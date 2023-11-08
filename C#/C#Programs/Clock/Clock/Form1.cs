using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Media;
using System.Xml;

namespace Clock
{
    public partial class Form1 : Form
    {
        int backGroundTasks = 0;
        public Form1()
        {
            InitializeComponent();
            this.Icon = Properties.Resources.ClockIcon;
        }
        
        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            string theDate = dateTimePicker1.Value.ToShortDateString();
            string hours = numericUpDown1.Value.ToString();
            string minutes = numericUpDown2.Value.ToString();
            string seconds = numericUpDown3.Value.ToString();
            if (seconds.Length == 1)
            {
                seconds = "0" + seconds;
            }
            if (minutes.Length == 1)
            {
                minutes = "0" + minutes;
            }
            string completeTime = hours + ":" + minutes + ":" + seconds;
            while (true)
            {
                
                DateTime localDate = DateTime.Now;
                string TimeNow = Convert.ToString(localDate);
                string CurrentDate = TimeNow.Split(' ')[0];
                string CurrentTime = TimeNow.Split(' ')[1];
                if (CurrentDate == theDate)
                {
                    if (CurrentTime == completeTime)
                    {
                        if (checkBox1.Checked)
                        {
                            Console.WriteLine("Time up!");
                            SoundPlayer playerFade = new SoundPlayer(Properties.Resources.alarm_fadein);
                            playerFade.Play();
                            backGroundTasks--;
                            break;
                        }
                        else
                        {
                            Console.WriteLine("Time up!");
                            SoundPlayer player = new SoundPlayer(Properties.Resources.alarm_sound);
                            player.Play();
                            backGroundTasks--;
                            break;
                        }
                    }
                }
                else
                {
                    continue;
                }
            }
        }
        private void backgroundWorker2_DoWork(object sender, DoWorkEventArgs e)
        {
            string theDate2 = dateTimePicker1.Value.ToShortDateString();
            string hours2 = numericUpDown1.Value.ToString();
            string minutes2 = numericUpDown2.Value.ToString();
            string seconds2 = numericUpDown3.Value.ToString();
            if (seconds2.Length == 1)
            {
                seconds2 = "0" + seconds2;
            }
            if (minutes2.Length == 1)
            {
                minutes2 = "0" + minutes2;
            }
            string completeTime2 = hours2 + ":" + minutes2 + ":" + seconds2;
            while (true)
            {

                DateTime localDate2 = DateTime.Now;
                string TimeNow2 = Convert.ToString(localDate2);
                string CurrentDate2 = TimeNow2.Split(' ')[0];
                string CurrentTime2 = TimeNow2.Split(' ')[1];
                if (CurrentDate2 == theDate2)
                {
                    if (CurrentTime2 == completeTime2)
                    {
                        if (checkBox1.Checked)
                        {
                            Console.WriteLine("Time up!");
                            SoundPlayer playerFade2 = new SoundPlayer(Properties.Resources.alarm_fadein);
                            playerFade2.Play();
                            backGroundTasks--;
                            break;
                        }
                        else
                        {
                            Console.WriteLine("Time up!");
                            SoundPlayer player2 = new SoundPlayer(Properties.Resources.alarm_sound);
                            player2.Play();
                            backGroundTasks--;
                            break;
                        }
                    }
                }
                else
                {
                    continue;
                }
            }
        }
        private void roundButton1_Click(object sender, EventArgs e)
        {
            panel2.Visible = true;
            
        }
        private void button5_Click(object sender, EventArgs e)
        {
            string theDate2 = dateTimePicker1.Value.ToShortDateString();
            string hours2 = numericUpDown1.Value.ToString();
            string minutes2 = numericUpDown2.Value.ToString();
            string seconds2 = numericUpDown3.Value.ToString();
            if (seconds2.Length == 1)
            {
                seconds2 = "0" + seconds2;
            }
            if (minutes2.Length == 1)
            {
                minutes2 = "0" + minutes2;
            }
            string completeTime2 = hours2 + ":" + minutes2 + ":" + seconds2;
            panel2.Visible = false;
            if (backGroundTasks == 0)
            {
                backgroundWorker1.RunWorkerAsync();
                backGroundTasks++;
                MessageBox.Show("Alarm set successfully");
            }
            else if(backGroundTasks == 1)
            {
                backgroundWorker2.RunWorkerAsync();
                backGroundTasks++;
                MessageBox.Show("Alarm set successfully");
            }
            else
            {
                MessageBox.Show("The maximum alarms that can be set at a time is 2. Redirecting you to a new instance of this App. So you can set 2 alarms more. ");
                Form fNew = new Form1();
                fNew.Show();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                SoundPlayer player = new SoundPlayer(Properties.Resources.alarm_fadein);
                player.Play();
            }
            else
            {
                SoundPlayer player = new SoundPlayer(Properties.Resources.alarm_sound);
                player.Play();
            }
        }
    }
    public class RoundButton : Button
    {
        protected override void OnPaint(System.Windows.Forms.PaintEventArgs e)
        {
            GraphicsPath grPath = new GraphicsPath();
            grPath.AddEllipse(0, 0, ClientSize.Width, ClientSize.Height);
            this.Region = new System.Drawing.Region(grPath);
            base.OnPaint(e);
        }
    }
}
