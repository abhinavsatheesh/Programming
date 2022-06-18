using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace QueueManager
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(textBox2.Text, "[^0-9]"))
            {
                textBox2.Text = textBox2.Text.Remove(textBox2.Text.Length - 1);
            }
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(textBox3.Text, "[^0-9]"))
            {
                textBox3.Text = textBox3.Text.Remove(textBox3.Text.Length - 1);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string nameper = textBox1.Text;
            string ageper = textBox2.Text;
            string mobileper = textBox3.Text;
            string emailidper = textBox4.Text;
            string addressper = richTextBox1.Text;
            string completeuserdata = "Name : " + nameper + "\nAge : " + ageper + "\nMobile Number : " + mobileper + "\nEmail ID : " + emailidper + "\nAddress : " + addressper;
            string root = System.IO.Path.GetDirectoryName(Application.ExecutablePath);
            string subpath = "UserData";
            string completefolderpath = Path.Combine(root, subpath);
            if (!Directory.Exists(completefolderpath))
            {
                Directory.CreateDirectory(completefolderpath);
            }
            string filename = nameper + ".txt";
            string completefilepath = Path.Combine(completefolderpath, filename);
            File.WriteAllText(completefilepath, completeuserdata);
            MessageBox.Show("User Data recorded successfully");
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            richTextBox1.Text = "";
        }
    }
}
