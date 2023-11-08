package com.example.passwordgenerator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView
import android.content.ClipboardManager

import android.content.ClipData
import android.content.Context
import android.os.Build
import android.widget.Toast


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
    fun Context.copyToClipboard(text: CharSequence){
        val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
        val clip = ClipData.newPlainText("label",text)
        clipboard.setPrimaryClip(clip)
    }
    fun generatePassword(view: View) {
        val adjectives = listOf("enormous", "doglike", "silly", "yellow", "fun", "fast", "beautiful", "sleepy", "slow", "smelly","wet", "fat", "red","orange", "yellow", "green",
            "blue", "purple", "fluffy","white", "proud", "brave", "adorable", "amused", "annoying", "ashamed", "awful", "better", "bloody", "blushing", "brave", "busy")
        val nouns = listOf("apple", "dinosaur", "ball","toaster", "goat", "dragon","hammer", "duck", "panda", "more", "some ", "telephone", "banana", "teacher")
        val specialchars = listOf("!", "@", "#", "$", "%", "^", "&", "*", "(", ")")
        val randAdjective = adjectives.random()
        val randNoun = nouns.random()
        val randNum = (0..10).random()
        val randSpecialChar = specialchars.random()
        val generatedPassword = randAdjective+randNoun+randNum+randSpecialChar
        val textViewBox: TextView = findViewById(R.id.textView4) as TextView
        val completeMessage:String = "Your new password is $generatedPassword"
        textViewBox.text = completeMessage
    }
    fun copyPassword(view: View) {
        val textViewBox: TextView = findViewById(R.id.textView4) as TextView
        val complete = textViewBox.text
        val delimter = "Your new password is "
        val completePasswordToCopy = complete.split(delimter)[1]
        copyToClipboard(completePasswordToCopy)
        val text = "Password copied successfully"
        val duration = Toast.LENGTH_SHORT
        val toast = Toast.makeText(applicationContext, text, duration)
        toast.show()
    }
}