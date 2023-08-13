//
//  ControlView.swift
//  green-house-app
//
//  Created by Jonas Jansen on 21.04.23.
//

import SwiftUI
import Firebase

struct ControlView: View {
    @ObservedObject var model = OverrideModel()
    
    var body: some View {
        VStack{
            VStack {
                HStack {
                    Text("Light")
                    Spacer()
                    Button(action: {
                        // Turn light on
                        model.updateData(documentId: "override_light", status: 1, counter: 1)
                    }, label: {
                        Text("On")
                    }).buttonStyle(.bordered).frame(width: 75)
                    Button(action: {
                        // Turn light off
                        model.updateData(documentId: "override_light", status: 0, counter: 1)
                    }, label: {
                        Text("Off")
                    }).buttonStyle(.bordered).frame(width: 75)
                }
            }
            VStack {
                HStack {
                    Text("Heating")
                    Spacer()
                    Button(action: {
                        // Turn heating on
                        model.updateData(documentId: "override_heating", status: 1, counter: 1)
                    }, label: {
                        Text("On")
                    }).buttonStyle(.bordered).frame(width: 75)
                    Button(action: {
                        // Turn heating on
                        model.updateData(documentId: "override_heating", status: 0, counter: 1)
                    }, label: {
                        Text("Off")
                    }).buttonStyle(.bordered).frame(width: 75)
                }
            }
            VStack {
                HStack {
                    Text("Humidity")
                    Spacer()
                    Button(action: {
                        // Open window
                        model.updateData(documentId: "override_humidity", status: 1, counter: 1)
                    }, label: {
                        Text("On")
                    }).buttonStyle(.bordered).frame(width: 75)
                    Button(action: {
                        // Close window
                        model.updateData(documentId: "override_humidity", status: 0, counter: 1)
                    }, label: {
                        Text("Off")
                    }).buttonStyle(.bordered).frame(width: 75)
                }
            }
            VStack {
                HStack {
                    Text("Watering")
                    Spacer()
                    Button(action: {
                        // Open window
                        model.updateData(documentId: "override_watering", status: 1, counter: 1)
                    }, label: {
                        Text("On")
                    }).buttonStyle(.bordered).frame(width: 75)
                    Button(action: {
                        // Close window
                        model.updateData(documentId: "override_watering", status: 0, counter: 1)
                    }, label: {
                        Text("Off")
                    }).buttonStyle(.bordered).frame(width: 75)
                }
            }
            VStack {
                HStack {
                    Text("Window")
                    Spacer()
                    Button(action: {
                        // Open window
                        model.updateData(documentId: "override_window", status: 1, counter: 1)
                    }, label: {
                        Text("Open")
                    }).buttonStyle(.bordered).frame(width: 75)
                    Button(action: {
                        // Close window
                        model.updateData(documentId: "override_window", status: 0, counter: 1)
                    }, label: {
                        Text("Close")
                    }).buttonStyle(.bordered).frame(width: 75)
                }
            }
        }.frame(maxWidth: 250)
    }
}
