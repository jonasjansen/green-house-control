//
//  ViewModelEnvironment.swift
//  green-house-app
//
//  Created by Jonas Jansen on 21.04.23.
//

import Foundation
import Firebase
import SwiftUI
import FirebaseStorage
import SDWebImageSwiftUI


class EnvironmentModel: ObservableObject {
    @Published var item  = Environment( id:"", heating_state:"", humidity:"", light_state:"", moisture:"", temperature:"", image_path:"", window_state:"", classify_result:"")
        
    func getData()
    {
        // Get a reference to the database
        let db = Firestore.firestore()
        db.collection("environment").order(by: "timestamp", descending: true).limit(to: 1)
            .addSnapshotListener {
                querySnapshot, error in
                guard let documents = querySnapshot?.documents else {
                    print("Error fetching documents: \(error!)")
                    return
                }
                let d = documents.first
                if let d = d {
                    self.item =  Environment(
                        id: d.documentID,
                        heating_state: d["heating_state"] as? String ?? "",
                        humidity: d["humidity"] as? String ?? "",
                        light_state: d["light_state"] as? String ?? "",
                        moisture: d["moisture"] as? String ?? "",
                        temperature: d["temperature"] as? String ?? "",
                        image_path: d["image_path"] as? String ?? "",
                        window_state: d["window_state"] as? String ?? "",
                        classify_result: d["classify_result"] as? String ?? ""
                    )
                }
        }
    }
}
