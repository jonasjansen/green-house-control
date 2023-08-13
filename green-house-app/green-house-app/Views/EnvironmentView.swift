//
//  EnvironmentView.swift
//  green-house-app
//
//  Created by Jonas Jansen on 21.04.23.
//

import SwiftUI
import Firebase

struct EnvironmentView: View {
    
    @ObservedObject var model = EnvironmentModel()
    @State var name = ""
    @State var notes = ""

    
    var body: some View {
        VStack(spacing: 15) {
            Divider()
            HStack {
                Text("Temperature:")
                Spacer()
                Text(model.item.temperature)
            }
            Divider()
            HStack {
                Text("Humidity:")
                Spacer()
                Text(model.item.humidity)
            }
        }.frame(maxWidth: 250)
        VStack(spacing: 15) {
            Divider()
            HStack {
                Text("Moisture:")
                Spacer()
                Text(model.item.moisture)
            }
            Divider()
            HStack {
                Text("Light:")
                Spacer()
                Text(model.item.light_state)
            }
        }.frame(maxWidth: 250)
        VStack(spacing: 15) {
            Divider()
            HStack {
                Text("Heating:")
                Spacer()
                Text(model.item.heating_state)
            }
            Divider()
            HStack {
                Text("Window:")
                Spacer()
                Text(model.item.window_state)
            }
        }.frame(maxWidth: 250)
        VStack(spacing: 15) {
            Divider()
            HStack {
                Text("Classify:")
                Spacer()
                Text(model.item.classify_result)
            }
            Divider()
        }.frame(maxWidth: 250)
    }
    init() {
        model.getData()
    }
}
