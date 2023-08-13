//
//  ViewModelEnvironment.swift
//  green-house-app
//
//  Created by Jonas Jansen on 21.04.23.
//

import Foundation
import Firebase

class OverrideModel: ObservableObject {
    func updateData(documentId: String, status: Int, counter: Int) {
        
        // Get a reference to the database
        let db = Firestore.firestore()
        let now = Date()
        let formatter = DateFormatter()
        formatter.timeZone = TimeZone.current
        formatter.dateFormat = "yyyy-MM-dd HH:mm:ss"
        let dateString = formatter.string(from: now)
        
        // Set the data to update
        db.collection("override").document(documentId).setData(["status":status, "counter": counter, "timestamp": dateString])
    }
}
