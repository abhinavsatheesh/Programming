using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace LeapYearChecker
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void TextBox1_TextChanged(object sender, TextChangedEventArgs e)
        {
            if (System.Text.RegularExpressions.Regex.IsMatch(TextBox1.Text, "[^0-9]"))
            {
                TextBox1.Text = TextBox1.Text.Remove(TextBox1.Text.Length - 1);
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            int yearentered = Convert.ToInt16(TextBox1.Text);
            string yearentereduser = TextBox1.Text;
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
            TextBox1.Text = "";
        }
        private void OnKeyDownHandler(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Return)
            {
                int yearentered = Convert.ToInt16(TextBox1.Text);
                string yearentereduser = TextBox1.Text;
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
                TextBox1.Text = "";
            }
        }

    }
}
