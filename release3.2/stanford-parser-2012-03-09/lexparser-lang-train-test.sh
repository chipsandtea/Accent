#!/usr/bin/env bash
#
# Defines standard configurations for training and evaluating the
# multilingual parsers (Arabic, Chinese, German, French). You can
# also train and test the English parsers with this script.
#
# For details on the language-specific options, see the javadocs and
# lexparser_lang.def.
#

# Memory limit
mem=10g

if [ ! $# -ge 5 ]; then
   echo Usage: `basename $0` lang len train_file test_file out_file features
   echo
   echo '  lang       : Language to parse (Arabic, English, Chinese, German, French)'
   echo '  len        : Maximum length of the sentences to parse'
   echo '  train_file : Training treebank file'
   echo '  test_file  : Test treebank file (for evaluation)'
   echo '  out_file   : Prefix for the output filename'
   echo '  features   : Variable length list of optional parser features'
   echo
   echo 'Parser memory limit is currently:' "$mem"
   echo   
   exit
fi

# Setup command-line options
lang=$1
len=$2
train_path=$3
test_file=$4
out_name=$5

shift 5

# Language-specific configuration
scriptdir=`dirname $0`
source $scriptdir/lexparser_lang.def

# Setting classpath
CLASSPATH="$CLASSPATH":"$scriptdir/*"

# Run the Stanford parser
java -server -Xmx"$mem" -Xms"$mem" edu.stanford.nlp.parser.lexparser.LexicalizedParser -v -maxLength "$len" \
-tLPP "$tlp" $lang_opts $* -writeOutputFiles \
-outputFilesExtension "$out_name"."$len".stp -outputFormat "penn" \
-outputFormatOptions "removeTopBracket,includePunctuationDependencies" -train "$train_path" -test "$test_file"
