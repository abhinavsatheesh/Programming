using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LeapYearChecker
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(textBox1.Text, "[^0-9]"))
            {
                textBox1.Text = textBox1.Text.Remove(textBox1.Text.Length - 1);
            }
        }
        

        private void button1_Click(object sender, EventArgs e)
        {
            int yearentered = Convert.ToInt16(textBox1.Text);
            string yearentereduser = textBox1.Text;
            if (yearentered % 4 == 0)
            {
                if (yearentered % 100 == 0)
                {
                    if (yearentered % 400 == 0)
                    {
                        MessageBox.Show(yearentereduser + " is a Leap Year");
                    }
                    else
                    {
                        MessageBox.Show(yearentereduser + " is not a Leap Year");
                    }
                }
                else
                {
                    MessageBox.Show(yearentereduser + " is a Leap Year");
                }
            }
            else
            {
                MessageBox.Show(yearentereduser + " is not a Leap Year");
            }
            textBox1.Text = "";
        }
        private void CheckEnterKeyPress(object sender, System.Windows.Forms.KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Return)

            {
                int yearentered = Convert.ToInt16(textBox1.Text);
                string yearentereduser = textBox1.Text;
                if (yearentered % 4 == 0)
                {
                    if (yearentered % 100 == 0)
                    {
                        if (yearentered % 400 == 0)
                        {
                            MessageBox.Show(yearentereduser + " is a Leap Year");
                        }
                        else
                        {
                            MessageBox.Show(yearentereduser + " is not a Leap Year");
                        }
                    }
                    else
                    {
                        MessageBox.Show(yearentereduser + " is a Leap Year");
                    }
                }
                else
                {
                    MessageBox.Show(yearentereduser + " is not a Leap Year");
                }
                textBox1.Text = "";
            }
        }
    }
}
