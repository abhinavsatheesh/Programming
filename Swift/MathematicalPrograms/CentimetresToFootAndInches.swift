//Convert your height from centimetres to inches and feet
import Swift
print("Enter your height")
let height = Float(readLine(strippingNewline: true)!)!
let heightininch = height/2.54
let heightinfeet = height/30.48
print("Height in inches = \(heightininch)")
print("Height in feet = \(heightinfeet)")
