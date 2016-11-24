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

class CorrectionViewController: UIViewController {

    var user = User(
        firstname:  "",
        lastname:   "",
        id:         "",
        password:   "",
        email:      "email@email.com"
    )
    @IBOutlet var correctedSentenceTextField: UITextView!
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
        let parameters : [String : String] = [
            "speech"    : sentenceTextField.text!,
            "email"     : user.email
        ]
        
        print(parameters)
        
        Alamofire.request("http://159.203.233.58/accent/default/api/sentence", method: .post, parameters: parameters, encoding: URLEncoding.default)
            .responseString { response in
                print(response)
                //let json = JSON(data: response.data!)
                
                
        }
    }
}
