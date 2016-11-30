//
//  PastQueriesViewController.swift
//  Accent
//
//  Created by Aidan Gadberry on 11/29/16.
//  Copyright © 2016 agadberr. All rights reserved.
//

import UIKit
import Alamofire
import SwiftyJSON

class PastQueriesViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {

    var user = [User]()
    var queries = [Query]()
    
    @IBOutlet var getQueriesButton: UIButton!
    @IBOutlet var queriesTableView: UITableView!
    
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

    @IBAction func getQueriesButtonPressed(_ sender: AnyObject) {
        self.getPastQueries()
    }
    
    
    func getPastQueries() {
        var url = "http://159.203.233.58/accent/default/api/"
        url += user[0].email + "/get"
        
        Alamofire.request(url, method: .get, encoding: URLEncoding.default)
            .responseJSON { response in
                print(response)
                
                let json = JSON(data: response.data!)
                print(json)
                
                for (_, jsonQuery) in json["content"] {
                    self.queries.append(
                        Query (
                            original: jsonQuery["speech"].stringValue,
                            corrected: jsonQuery["corrected"].stringValue
                        )
                    )
                    print(jsonQuery)
                }
        }
        
    }
    
    // Table View Protocol
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = queriesTableView.dequeueReusableCell(withIdentifier: "QueriesTableViewCell") as! QueriesTableViewCell
        
        cell.originalText.text = queries[indexPath.row].original
        cell.correctedText.text = queries[indexPath.row].corrected
        return cell
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return queries.count
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 100.0
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
