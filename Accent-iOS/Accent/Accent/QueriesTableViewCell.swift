//
//  QueriesTableViewCell.swift
//  Accent
//
//  Created by Aidan Gadberry on 11/30/16.
//  Copyright © 2016 agadberr. All rights reserved.
//

import UIKit

class QueriesTableViewCell: UITableViewCell {

    @IBOutlet var originalText: UILabel!
    @IBOutlet var correctedText: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
