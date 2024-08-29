import SwiftUI
import UniformTypeIdentifiers
struct BlueButton: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .background(Color.red)
            .foregroundColor(.white)
            .clipShape(Capsule())
            .scaleEffect(configuration.isPressed ? 1.2 : 1)
            .animation(.easeOut(duration: 0.2), value: configuration.isPressed)
    }
}

struct ExportView: View 
{
    
    @State 
    private var isExporting = false
    @Environment(\.scenePhase) private var phase
    @State private var calculations: String = ""
    @State private var tt: String = ""
    @State private var calc: String = ""
    @State private var bracketopen: Bool = false
    @State private var showingPopover = false
    @State private var showingalert: Bool = false
    @State private var willMoveToNextScreen: Bool = false
    @State private var ipaFile: IPAFile?
    @State private var hasOperatorPlus: Bool = false
    @State private var hasOperatorMinus: Bool = false
    @State private var hasOperatorInto: Bool = false
    @State private var hasOperatorDivide: Bool = false
    var body: some View {
            VStack {
                HStack {
                    Text("Calculator")
                        .font(Font.custom("MyFont", size: 30))
                }
            }
            HStack {
                TextField("", text: $calculations)
                    .keyboardType(.numberPad)
                Button("Copy") {
                    UIPasteboard.general.string = calculations
                    showingalert = true
                    
                    
                }
                .alert("Copied to Clipboard", isPresented: $showingalert) {
                    Button("OK", role: .cancel) {}
                }
            }
            
            HStack {
                Button("7") {
                    calculations = calculations + "7"
                }
                .buttonStyle(BlueButton())
                Button("8") {
                    calculations = calculations + "8"
                }
                .buttonStyle(BlueButton())
                Button("9") {
                    calculations = calculations + "9"
                }
                
                .buttonStyle(BlueButton())
                Button("/") {
                    if calculations.last == "-" || calculations.last == "*" || calculations.last == "/" || calculations.last == "+"{
                        
                    }
                    else{
                        calculations = calculations + "/"
                        hasOperatorPlus=true
                    }
                }
                .buttonStyle(BlueButton())
                Button("Del") {
                    
                    let choppedString = String(calculations.dropLast())
                    let choopedchar = calculations.last
                    switch choopedchar{
                        case "+":
                        hasOperatorPlus=false
                        case "-":
                        hasOperatorMinus=false
                        case "*":
                        hasOperatorInto=false
                        case "/":
                        hasOperatorDivide=false
                    default:
                        print("")
                    }
                    calculations = choppedString
                }
                .buttonStyle(BlueButton())
            }
            HStack {
                Button("4") {
                    calculations = calculations + "4"
                }
                .buttonStyle(BlueButton())
                Button("5") {
                    calculations = calculations + "5"
                }
                .buttonStyle(BlueButton())
                Button("6") {
                    calculations = calculations + "6"
                }
                .buttonStyle(BlueButton())
                Button("-") {
                    if calculations.last == "-" || calculations.last == "*" || calculations.last == "/" || calculations.last == "+"{
                        
                    }
                    else{
                        calculations = calculations + "-"
                        hasOperatorMinus=true
                    }
                }
                .buttonStyle(BlueButton())
                Button("CE") {
                    calculations = ""
                }
                .buttonStyle(BlueButton())
            }
            HStack {
                Button("1") {
                    calculations = calculations + "1"
                }
                .buttonStyle(BlueButton())
                Button("2") {
                    calculations = calculations + "2"
                }
                .buttonStyle(BlueButton())
                Button("3") {
                    calculations = calculations + "3"
                }
                .buttonStyle(BlueButton())
                Button("x") {
                    if calculations.last == "-" || calculations.last == "*" || calculations.last == "/" || calculations.last == "+"{
                        
                    }
                    else{
                        calculations = calculations + "*"
                        hasOperatorInto=true
                    }
                }
                .buttonStyle(BlueButton())
                Button("()") {
                    if (bracketopen == false) {
                        bracketopen = true
                        calculations = calculations + "("
                    }
                    else if (bracketopen == true) {
                        bracketopen = false
                        calculations = calculations + ")"
                    }
                }
                .buttonStyle(BlueButton())
                
            }
            HStack {
                Button("0") {
                    
                    calculations = calculations + "0"
                }
                .buttonStyle(BlueButton())
                Button("00") {
                    calculations = calculations + "00"
                }
                .buttonStyle(BlueButton())
                Button(".") {
                    calculations = calculations + "."
                }
                .buttonStyle(BlueButton())
                Button("+") {
                    print(hasOperatorPlus)
                    
                        if calculations.last == "-" || calculations.last == "*" || calculations.last == "/" || calculations.last == "+"{
                            
                        }
                        else{
                            calculations = calculations + "+"
                            hasOperatorPlus=true
                        }
                    
                }
                .buttonStyle(BlueButton())
                Button("=") {
                    let exp: NSExpression = NSExpression(format: calculations)
                    let result: Double = exp.expressionValue(with:nil, context: nil) as! Double
                    calculations = String(result)
                    let myArray = calculations.split(separator: ".")
                    if myArray[1]=="0"{
                        calculations = String(myArray[0])
                    }
                    
                }
                .buttonStyle(BlueButton())
            }
    
        
        VStack(spacing: 25) {
            Button(action: export) { 
                Label("Export IPA", systemImage: "square.and.arrow.up")
                    .imageScale(.large)
                    .foregroundColor(.accentColor)
            }
        }
        .fileExporter(isPresented: self.$isExporting, document: self.ipaFile, contentType: .ipa) { result in
            print("Exported IPA:", result)
        }
        }
    
    private func export()
    {
        Task { @MainActor in            
            do
            {
                let ipaPath = try await exportIPA()
                let ipaURL = URL(fileURLWithPath: ipaPath)
                
                self.ipaFile = try IPAFile(ipaURL: ipaURL)
                self.isExporting = true
            }
            catch
            {
                print("Could not export .ipa:", error)
            }
        }
    }
}
