//
//  CorrectionViewController.swift
//  Accent
//
//  Created by Aidan Gadberry on 10/26/16.
//  Copyright © 2016 agadberr. All rights reserved.
//

import UIKit
import Speech
import AVFoundation
import Alamofire
import SwiftyJSON
import SCLAlertView

class CorrectionViewController: UIViewController {

    var user = [User]()
    
    @IBOutlet var correctedSentence: UILabel!
    @IBOutlet var sentenceTextField: UITextView!
    @IBOutlet var submitQueryButton: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func viewWillAppear(_ animated: Bool) {
        UIApplication.shared.statusBarStyle = .lightContent
    }
    
    override var preferredStatusBarStyle : UIStatusBarStyle {
        return .lightContent
    }
//
//    func requestSpeechAuthentication() {
//        
//    }
    @IBAction func submitButtonPressed(_ sender: AnyObject) {
        self.correctSpeech()
    }
    
    func correctSpeech() {
        print(user)
        let parameters : [String : String] = [
            "speech"    : sentenceTextField.text!.lowercased(),
            "email"     : user[0].email
        ]
        
        print(parameters)
        
        Alamofire.request("http://159.203.233.58/accent/default/api/sentence", method: .post, parameters: parameters, encoding: URLEncoding.default)
            .responseJSON { response in
                print(response)
                
                let json = JSON(data: response.data!)
                print(json)
                if (json["error"].stringValue != "") {
                    SCLAlertView().showError("Whoops!", subTitle: json["error"].stringValue)
                    
                } else {
                    self.correctedSentence.text = json["corrected"].stringValue
                }
                
        }
        
    }
}
