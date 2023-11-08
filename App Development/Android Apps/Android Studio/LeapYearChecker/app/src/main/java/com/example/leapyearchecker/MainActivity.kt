package com.example.leapyearchecker

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.TextView
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
    fun yearchecker(view: View) {
        val textView = findViewById<TextView>(R.id.editTextNumber)
        val str: String = textView.text.toString()
        val completeYear: Int = str.toInt()
        if (completeYear%4 == 0) {
            val messagetobe: String = str + " is a Leap Year"
            val text = messagetobe
            val duration = Toast.LENGTH_SHORT
            val toast = Toast.makeText(applicationContext, text, duration)
            toast.show()
            textView.text = ""
        }
        else {
            val messagetobe: String = str + " is not a Leap Year"
            val text = messagetobe
            val duration = Toast.LENGTH_SHORT
            val toast = Toast.makeText(applicationContext, text, duration)
            toast.show()
            textView.text = ""
        }
    }

}