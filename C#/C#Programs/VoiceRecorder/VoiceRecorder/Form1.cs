using System.Diagnostics;
using System;
using System.Windows.Forms;
using System.Collections;
using System.Drawing;
using Microsoft.VisualBasic;
using System.Data;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace VoiceRecorder
{

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        [DllImport("winmm.dll", EntryPoint = "mciSendStringA", ExactSpelling = true, CharSet = CharSet.Ansi, SetLastError = true)]
        static extern int record(string lpstrCommand, string lpstrReturnString, int uReturnLength, int hwndCallback);
        
        private void button1_Click(object sender, EventArgs e)
        {
            button2.Enabled = true;
            pictureBox1.Image = Properties.Resources.RecordingMic;
            timer1.Enabled = true;
            timer1.Start();
            record("open new Type waveaudio Alias recsound", "", 0, 0);
            record("record recsound", "", 0, 0);
            button1.Enabled = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Stop();
            timer1.Enabled = false;
            saveFileDialog1.ShowDialog();
            string fullSavePath = Path.GetFullPath(saveFileDialog1.FileName);
            record("save recsound " + fullSavePath, "", 0, 0);
            record("close recsound", "", 0, 0);
            button1.Enabled = true;
            button2.Enabled = false;
            pictureBox1.Image = Properties.Resources.MicIcon;
            MessageBox.Show("Recording saved in the path : " + fullSavePath);
        }
    }
}