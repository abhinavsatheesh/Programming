import SwiftUI
import WebKit

struct WebView: UIViewRepresentable {
    
    var url: URL
    
    func makeUIView(context: Context) -> WKWebView {
        return WKWebView()
    }
    
    func updateUIView(_ webView: WKWebView, context: Context) {
        let request = URLRequest(url: url)
        webView.load(request)
    }
}

struct ContentView: View {
    @State private var showWebView = false
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("IP Address Checker")
            Button {
                showWebView.toggle()
            } label: {
                Text("Show IP Address")
            }
            .sheet(isPresented: $showWebView) {
                WebView(url: URL(string: "https://api.ipify.org")!)
            }
            Text("By clicking the above button, we will get access to your IP Address. We will discard it immediately after your use")
        }
    }
}
