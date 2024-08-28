import SwiftUI

struct ContentView: View {
    @State var yearentered = ""
    @State var number = 0
    @State var showAlert = false
    @State var message = ""
    @State var NumLength = ""
    var body: some View {
        NavigationView {
        let _ = "If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5. The year is a leap year (it has 366 days). The year is not a leap year (it has 365 days)."
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Leap Year Checker")
            TextField("Enter an year", text: $yearentered)
                .keyboardType(.decimalPad)
                .padding(10)
            Button("Calculate") {
                number = Int(yearentered) ?? 0
                NumLength = String(number)
                if (NumLength.count <= 4) {
                    
                }
                if (number%4 == 0) {
                    if (number%100 == 0) {
                        if (number%400 == 0) {
                            showAlert = true
                            message = yearentered + " is a leap year"
                            yearentered = ""
                        }
                        else {
                            showAlert = true
                            message = yearentered + " is not a leap year"
                            yearentered = ""
                        }
                    }
                    else {
                        showAlert = true
                        message = yearentered + " is a leap year"
                        yearentered = ""
                    }
                }
                else {
                    showAlert = true
                    message = yearentered + " is not a leap year"
                    yearentered = ""
                }
            }
            NavigationLink {
                // destination view to navigation to
                ExportView()
            } label: {
                Image(systemName: "list.dash")
                    .foregroundColor(.gray)
            }
            .alert(message, isPresented: $showAlert) {
                Button("OK", role: .cancel) {}
            }
        }
    }
}
}

