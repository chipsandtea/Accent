//
//  LandingViewController.swift
//  Accent
//
//  Created by Aidan Gadberry on 10/26/16.
//  Copyright © 2016 agadberr. All rights reserved.
//

import UIKit
import TextFieldEffects
import Alamofire
import SCLAlertView
import SwiftyJSON

class LandingViewController: UIViewController {

    @IBOutlet var loginView: UIView!
    @IBOutlet var loginButton: UIButton!
    @IBOutlet var loginUsername: IsaoTextField!
    @IBOutlet var loginPassword: IsaoTextField!

    @IBOutlet var registerViewButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func viewWillAppear(_ animated: Bool) {
        UIApplication.shared.statusBarStyle = .lightContent
        self.navigationController?.isNavigationBarHidden = true
    }
    
    override var preferredStatusBarStyle : UIStatusBarStyle {
        return .lightContent
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func loginPressed(_ sender: AnyObject) {
        
        self.processLogin()
    }
    
    @IBAction func displayRegisterView(_ sender: AnyObject) {
        let registerVC = self.storyboard?.instantiateViewController(withIdentifier: "RegisterVC") as! RegisterViewController
        self.navigationController?.pushViewController(registerVC, animated: true)
    }
    
    func processLogin() {
        let parameters : [String : String] = [
            "email" : loginUsername.text!,
            "password" : loginPassword.text!
        ]
        
        print(parameters)
        
        var url = "http://159.203.233.58/accent/default/api/login/"
        url += parameters["email"]!
        url += "/"
        url += parameters["password"]!
        
        print(url)
        
        Alamofire.request(url, method: .get, encoding: URLEncoding.default)
            .responseJSON { response in
                
                print(response)
                
                let json = JSON(data: response.data!)
                
                if (json["error"].stringValue != "") {
                    SCLAlertView().showError("Whoops!", subTitle: json["error"].stringValue)

                } else {
                
                    let user = User(
                        firstname:  json["content"][0]["firstname"].stringValue,
                        lastname:   json["content"][0]["lastname"].stringValue,
                        id:         json["content"][0]["id"].stringValue,
                        password:   json["content"][0]["password"].stringValue,
                        email:      json["content"][0]["email"].stringValue
                    )
                    
                    
                    let correctionVC = self.storyboard?.instantiateViewController(withIdentifier: "CorrectionVC") as! CorrectionViewController
                    print(user)
                    correctionVC.user = user
                    
                    self.navigationController?.pushViewController(correctionVC, animated: true)
                }
             
//                if (response.result.isSuccess) {
//                    print("BIG SUCCESS")
//                } else {
//                    print("BIG ERROR")
//                }
                // SUCCESS: {"acc": {"errors": {}, "id": 15}, "status": "success"}
                
                
                
        }
    }
    
}

