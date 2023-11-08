namespace SatheeshFinancialDoubtSolver
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.panelMain = new System.Windows.Forms.Panel();
            this.button3 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.panelMain.SuspendLayout();
            this.SuspendLayout();
            // 
            // panelMain
            // 
            this.panelMain.Controls.Add(this.button3);
            this.panelMain.Controls.Add(this.button2);
            this.panelMain.Controls.Add(this.button1);
            this.panelMain.Controls.Add(this.label2);
            this.panelMain.Controls.Add(this.label1);
            this.panelMain.Location = new System.Drawing.Point(1, 0);
            this.panelMain.Name = "panelMain";
            this.panelMain.Size = new System.Drawing.Size(946, 343);
            this.panelMain.TabIndex = 5;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(368, 202);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(121, 43);
            this.button3.TabIndex = 9;
            this.button3.Text = "Accountancy";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(318, 268);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(235, 43);
            this.button2.TabIndex = 8;
            this.button2.Text = "Income Tax and Economics";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(368, 145);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(112, 34);
            this.button1.TabIndex = 7;
            this.button1.Text = "GST";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(114, 73);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(718, 50);
            this.label2.TabIndex = 6;
            this.label2.Text = "Hi. Welcome To The Satheesh Financial Doubt Solver. What do you need help with to" +
    "day?\n There are 3 options, GST, Income Tax and Economics and Accountancy.";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(308, 31);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(265, 25);
            this.label1.TabIndex = 5;
            this.label1.Text = "Satheesh Financial Doubt Solver";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(946, 343);
            this.Controls.Add(this.panelMain);
            this.Name = "Form1";
            this.Text = "Satheesh Financial Doubt Solver";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_Close);
            this.panelMain.ResumeLayout(false);
            this.panelMain.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private Panel panelMain;
        private Button button3;
        private Button button2;
        private Button button1;
        private Label label2;
        private Label label1;
    }
}