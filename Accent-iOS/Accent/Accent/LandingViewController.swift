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
        let speechVC = self.storyboard?.instantiateViewController(withIdentifier: "SpeechVC") as! SpeechViewController
        
        self.navigationController?.pushViewController(speechVC, animated: true)
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
        
        Alamofire.request("http://159.203.233.58/accent/default/api/login", method: .post, parameters: parameters, encoding: URLEncoding.default)
            .responseString { response in
                
                print(response)
                
                SUCCESS: {"acc": {"errors": {}, "id": 15}, "status": "success"}
                
                
                
        }
    }
    
}

