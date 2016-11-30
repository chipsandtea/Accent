//
//  RegisterViewController.swift
//  Accent
//
//  Created by Aidan Gadberry on 11/2/16.
//  Copyright © 2016 agadberr. All rights reserved.
//

import UIKit
import TextFieldEffects
import Alamofire
import SwiftyJSON
import SCLAlertView

class RegisterViewController: UIViewController {
    
    @IBOutlet var registerFirstName: IsaoTextField!
    @IBOutlet var registerLastName: IsaoTextField!
    @IBOutlet var registerEmail: IsaoTextField!
    @IBOutlet var registerPassword: IsaoTextField!
    
    
    @IBOutlet var registerButton: UIButton!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func viewWillAppear(_ animated: Bool) {
        self.navigationController?.isNavigationBarHidden = false
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func submitRegisterForm(_ sender: AnyObject) {
        
//        let account = Account (
//            firstname: registerUsername.text!,
//            lastname: registerUsername.text!,
//            password: registerPassword.text!,
//            email: registerEmail.text!
//        )
        
        let parameters : [String : String] = [
            "firstname" : registerFirstName.text!,
            "lastname"  : registerLastName.text!,
            "password"  : registerPassword.text!,
            "email"     : registerEmail.text!
        ]
        
        print(parameters)
        
        Alamofire.request("http://159.203.233.58/accent/default/api/acc", method: .post, parameters: parameters, encoding: URLEncoding.default)
            .responseJSON { response in
                
                print(response)
                
                let json = JSON(data: response.data!)
                
                if (json["error"].stringValue != "") {
                    SCLAlertView().showError("Whoops!", subTitle: json["error"].stringValue)
                    
                } else {
                    let landingVC = self.storyboard?.instantiateViewController(withIdentifier: "LandingVC") as! LandingViewController
                    self.navigationController?.pushViewController(landingVC, animated: true)
                }
                
                
        }
        
    }

    func finishRegister(first_token : String, second_token : String) {
        
    }
    
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
