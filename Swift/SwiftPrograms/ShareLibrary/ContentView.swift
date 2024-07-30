import SwiftUI
import UIKit

struct ContentView: View {
    func topViewController()-> UIViewController{
        var topViewController:UIViewController = UIApplication.shared.keyWindow!.rootViewController!
        
        while ((topViewController.presentedViewController) != nil) {
            topViewController = topViewController.presentedViewController!;
        }
        
        return topViewController
    }
    
    func showShareActivity(msg:String?, image:UIImage?, url:String?, sourceRect:CGRect?){
        var objectsToShare = [AnyObject]()
        
        if let url = url {
            objectsToShare = [url as AnyObject]
        }
        
        if let image = image {
            objectsToShare = [image as AnyObject]
        }
        
        if let msg = msg {
            objectsToShare = [msg as AnyObject]
        }
        
        let activityVC = UIActivityViewController(activityItems: objectsToShare, applicationActivities: nil)
        activityVC.modalPresentationStyle = .popover
        activityVC.popoverPresentationController?.sourceView = topViewController().view
        if let sourceRect = sourceRect {
            activityVC.popoverPresentationController?.sourceRect = sourceRect
        }
        
        topViewController().present(activityVC, animated: true, completion: nil)
    }
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
            Button("Share") {
                showShareActivity(msg:"Test", image: nil, url: nil, sourceRect: nil) 
        }}
    }
}
