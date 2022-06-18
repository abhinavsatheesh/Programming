using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace Calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.Icon = Properties.Resources.CalculatorIcon;
        }
        public static string getBetween(string strSource, string strStart, string strEnd)
        {
            if (strSource.Contains(strStart) && strSource.Contains(strEnd))
            {
                int Start, End;
                Start = strSource.IndexOf(strStart, 0) + strStart.Length;
                End = strSource.IndexOf(strEnd, Start);
                return strSource.Substring(Start, End - Start);
            }

            return "";
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(textBox1.Text, "[^0-9]"))
            {
                textBox1.Text = textBox1.Text.Remove(textBox1.Text.Length - 1);
            }
            else
            {
                string lastChar = textBox1.Text.Substring(textBox1.Text.Length - 1, 1);
                if (lastChar == "+")
                {

                }
                else if (lastChar == "-")
                {

                }
                else if (lastChar == "*")
                {

                }
                else if (lastChar == "/")
                {

                }
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            this.AutoSize = true;
        }
        private void AddTextToTextBox(string Num)
        {
            textBox1.Text += Num;
        }
        private void label1_Click(object sender, EventArgs e)
        {
            Form about = new AboutBox1();
            about.ShowDialog();
        }
        private void ButtonNum1_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("1");
        }
        private void ButtonNum2_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("2");
        }
        private void ButtonNum3_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("3");
        }
        private void ButtonNum4_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("4");
        }
        private void ButtonNum5_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("5");
        }
        private void ButtonNum6_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("6");
        }
        private void ButtonNum7_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("7");
        }
        private void ButtonNum8_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("8");
        }
        private void ButtonNum9_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("9");
        }
        private void ButtonNum0_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("0");
        }
        private void ButtonNumPlus_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("+");
        }
        private void ButtonNumMinus_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("-");
        }
        private void ButtonNumMultiply_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("X");
        }
        private void ButtonNumDivide_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("÷");
        }
        private void ButtonDecimal_Click(object sender, EventArgs e)
        {
            AddTextToTextBox(".");
        }
        private void ButtonNumPercentage_Click(object sender, EventArgs e)
        {
            AddTextToTextBox("%");
        }
        private void ButtonBackSpace_Click(object sender, EventArgs e)
        {
            try
            {
                textBox1.Text = textBox1.Text.Substring(0, textBox1.Text.Length - 1);
            }
            catch
            {

            }
        }
        private void ButtonCE_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
        }
        private void ButtonAddMinus_Click(object sender, EventArgs e)
        {
            try
            {
                string result = textBox1.Text.Substring(0, 1);
                if (textBox1.Text.StartsWith("-"))
                {
                    
                    textBox1.Text = textBox1.Text.Remove(0, 1);
                }
                else
                {
                    textBox1.Text = "-" + textBox1.Text;
                }
            }
            catch
            {
                if (textBox1.Text == "")
                {
                    textBox1.Text = "-";
                }
            }
        }
        private void ButtonTextBoxSquared_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dt = new DataTable();
                string CalculationToBe = textBox1.Text;
                string newSplit = CalculationToBe.Replace("X", "*");
                string newNewSplit = newSplit.Replace("÷", "/");
                if (newNewSplit.Contains("%"))
                {
                    string data = getBetween(newNewSplit, "*", "%");
                    if (data == "")
                    {
                        data = getBetween(newNewSplit, "+", "%");

                        if (data == "")
                        {
                            data = getBetween(newNewSplit, "-", "%");
                            if (data == "")
                            {
                                data = getBetween(newNewSplit, "/", "%");
                            }
                        }
                    }
                    string completeData = data + "%";
                    double NumToBe = (Convert.ToDouble(data)) / 100;
                    string FinalNumToBED = Convert.ToString(NumToBe);
                    string TOBE = newNewSplit.Replace(completeData, FinalNumToBED);
                    var v = dt.Compute(TOBE, "");
                    double FinalCalculationResult = Convert.ToDouble(v);
                    double FinalResult = Math.Pow(FinalCalculationResult, 2);
                    textBox1.Text = Convert.ToString(FinalResult);
                }
                else
                {
                    string TOBE = newNewSplit;
                    var v = dt.Compute(TOBE, "");
                    double FinalCalculationResult = Convert.ToDouble(v);
                    double FinalResult = Math.Pow(FinalCalculationResult, 2);
                    textBox1.Text = Convert.ToString(FinalResult);
                }
            }
            catch
            {
                MessageBox.Show("An unexpected error occured");
                textBox1.Text = "";
            }
        }
        private void ButtonDivide1ByTextBox_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dt = new DataTable();
                string CalculationToBe = textBox1.Text;
                string newSplit = CalculationToBe.Replace("X", "*");
                string newNewSplit = newSplit.Replace("÷", "/");
                if (newNewSplit.Contains("%"))
                {
                    string data = getBetween(newNewSplit, "*", "%");
                    if (data == "")
                    {
                        data = getBetween(newNewSplit, "+", "%");

                        if (data == "")
                        {
                            data = getBetween(newNewSplit, "-", "%");
                            if (data == "")
                            {
                                data = getBetween(newNewSplit, "/", "%");
                            }
                        }
                    }
                    string completeData = data + "%";
                    double NumToBe = (Convert.ToDouble(data)) / 100;
                    string FinalNumToBED = Convert.ToString(NumToBe);
                    string TOBE = newNewSplit.Replace(completeData, FinalNumToBED);
                    var v = dt.Compute(TOBE, "");
                    double FinalCalculationResult = Convert.ToDouble(v);
                    string DivideFurther = "1/" + FinalCalculationResult;
                    var vDivide = dt.Compute(DivideFurther, "");
                    string FinalCalculation = Convert.ToString(vDivide);
                    textBox1.Text = FinalCalculation;
                }
                else
                {
                    string TOBE = newNewSplit;
                    var v = dt.Compute(TOBE, "");
                    double FinalCalculationResult = Convert.ToDouble(v);
                    string DivideFurther = "1/" + FinalCalculationResult;
                    var vDivide = dt.Compute(DivideFurther, "");
                    string FinalCalculation = Convert.ToString(vDivide);
                    textBox1.Text = FinalCalculation;
                }
            }
            catch
            {
                MessageBox.Show("An unexpected error occured");
                textBox1.Text = "";
            }
        }
        private void ButtonRootTextBox_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dt = new DataTable();
                string CalculationToBe = textBox1.Text;
                string newSplit = CalculationToBe.Replace("X", "*");
                string newNewSplit = newSplit.Replace("÷", "/");
                if (newNewSplit.Contains("%"))
                {
                    string data = getBetween(newNewSplit, "*", "%");
                    if (data == "")
                    {
                        data = getBetween(newNewSplit, "+", "%");

                        if (data == "")
                        {
                            data = getBetween(newNewSplit, "-", "%");
                            if (data == "")
                            {
                                data = getBetween(newNewSplit, "/", "%");
                            }
                        }
                    }
                    string completeData = data + "%";
                    double NumToBe = (Convert.ToDouble(data)) / 100;
                    string FinalNumToBED = Convert.ToString(NumToBe);
                    string TOBE = newNewSplit.Replace(completeData, FinalNumToBED);
                    var v = dt.Compute(TOBE, "");
                    double FinalCalculationResult = Convert.ToDouble(v);
                    double FinalCalculation = Math.Sqrt(FinalCalculationResult);
                    textBox1.Text = Convert.ToString(FinalCalculation);
                }
                else
                {
                    string TOBE = newNewSplit;
                    var v = dt.Compute(TOBE, "");
                    double FinalCalculationResult = Convert.ToDouble(v);
                    double FinalCalculation = Math.Sqrt(FinalCalculationResult);
                    textBox1.Text = Convert.ToString(FinalCalculation);
                }
            }
            catch
            {
                MessageBox.Show("An unexpected error occured");
                textBox1.Text = "";
            }
        }
        
        private void ButtonEvaluate_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dt = new DataTable();
                string CalculationToBe = textBox1.Text;
                string newSplit = CalculationToBe.Replace("X", "*");
                string newNewSplit = newSplit.Replace("÷", "/");
                if (newNewSplit.Contains("%")) {
                    string data = getBetween(newNewSplit, "*", "%");
                    if (data == "")
                    {
                        data = getBetween(newNewSplit, "+", "%");

                        if (data == "")
                        {
                            data = getBetween(newNewSplit, "-", "%");
                            if (data == "")
                            {
                                data = getBetween(newNewSplit, "/", "%");
                            }
                        }
                    }
                    string completeData = data + "%";
                    double NumToBe = (Convert.ToDouble(data)) / 100;
                    string FinalNumToBED = Convert.ToString(NumToBe);
                    string TOBE = newNewSplit.Replace(completeData, FinalNumToBED);
                    var v = dt.Compute(TOBE, "");
                    string FinalCalculationResult = Convert.ToString(v);
                    textBox1.Text = FinalCalculationResult;
                }
                else
                {
                    string TOBE = newNewSplit;
                    var v = dt.Compute(TOBE, "");
                    string FinalCalculationResult = Convert.ToString(v);
                    textBox1.Text = FinalCalculationResult;
                }
            }
            catch
            {
                MessageBox.Show("An unexpected error occured");
                textBox1.Text = "";
            }
        }

        private void CheckEnterKey(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Return)
            {
                try
                {
                    DataTable dt = new DataTable();
                    string CalculationToBe = textBox1.Text;
                    string newSplit = CalculationToBe.Replace("X", "*");
                    string newNewSplit = newSplit.Replace("÷", "/");
                    if (newNewSplit.Contains("%"))
                    {
                        string data = getBetween(newNewSplit, "*", "%");
                        if (data == "")
                        {
                            data = getBetween(newNewSplit, "+", "%");

                            if (data == "")
                            {
                                data = getBetween(newNewSplit, "-", "%");
                                if (data == "")
                                {
                                    data = getBetween(newNewSplit, "/", "%");
                                }
                            }
                        }
                        string completeData = data + "%";
                        double NumToBe = (Convert.ToDouble(data)) / 100;
                        string FinalNumToBED = Convert.ToString(NumToBe);
                        string TOBE = newNewSplit.Replace(completeData, FinalNumToBED);
                        var v = dt.Compute(TOBE, "");
                        string FinalCalculationResult = Convert.ToString(v);
                        textBox1.Text = FinalCalculationResult;
                        textBox1.SelectionStart = textBox1.Text.Length;
                        textBox1.SelectionLength = 0;
                    }
                    else
                    {
                        string TOBE = newNewSplit;
                        var v = dt.Compute(TOBE, "");
                        string FinalCalculationResult = Convert.ToString(v);
                        textBox1.Text = FinalCalculationResult;
                        textBox1.SelectionStart = textBox1.Text.Length;
                        textBox1.SelectionLength = 0;
                    }
                }
                catch
                {
                    MessageBox.Show("An unexpected error occured");
                    textBox1.Text = "";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }
    }
}
