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
        url += parameters["email"]! + "/" + parameters["password"]!
        
        print(url)
        
        Alamofire.request(url, method: .get, encoding: URLEncoding.default)
            .responseJSON { response in
                let description = response.description
                print(response)
                if (description.substring(to: description.index(description.startIndex, offsetBy: 7)) == "FAILURE") {
                    SCLAlertView().showError("Whoops!", subTitle: "Error connecting to server")
                } else {
                    let json = JSON(data: response.data!)
                    
                    if (json["error"].stringValue != "") {
                        SCLAlertView().showError("Whoops!", subTitle: json["error"].stringValue)

                    } else {
                        var myUser = [User]()
                        let user = User(
                            firstname:  json["content"][0]["firstname"].stringValue,
                            lastname:   json["content"][0]["lastname"].stringValue,
                            id:         json["content"][0]["id"].stringValue,
                            password:   json["content"][0]["password"].stringValue,
                            email:      json["content"][0]["email"].stringValue
                        )
                        myUser.append(user)
                        
                        
                        let myDelegate = UIApplication.shared.delegate as! AppDelegate
                        myDelegate.switchToTabBar(user: myUser)
                    }
                }
        }
    }
    
}

