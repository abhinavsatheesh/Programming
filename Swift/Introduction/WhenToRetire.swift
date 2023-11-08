import Swift
print("Enter your Name")
let name = readLine()
print("Enter your Age")
let age = Int(readLine(strippingNewline: true)!)!
print("Enter your Profession")
let profession = readLine()
print("Enter your Retiring Age")
let retiringage = Int(readLine(strippingNewline : true)!)!
let yearsleft = retiringage-age
print("Hello \(name!). Your age is \(age). Your profession is \(profession!). You will have to retire from \(profession!) in \(yearsleft) years")