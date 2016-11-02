//
//  LandingViewController.swift
//  Accent
//
//  Created by Aidan Gadberry on 10/26/16.
//  Copyright © 2016 agadberr. All rights reserved.
//

import UIKit
import TextFieldEffects

class LandingViewController: UIViewController {

    @IBOutlet var loginView: UIView!
    @IBOutlet var loginButton: UIButton!
    @IBOutlet var loginUsername: JiroTextField!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.navigationController?.isNavigationBarHidden = true
        
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func viewWillAppear(_ animated: Bool) {
        UIApplication.shared.statusBarStyle = .lightContent
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
    
    
    
}

