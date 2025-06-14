using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Zadanhie4
{
    public partial class Form1 : Form
    {
        private int rectWidth;
        private int rectHeight;
        private Color rectColor;
        private bool canPaint = false;
        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            if (canPaint)
            {
                using (Brush brush = new SolidBrush(rectColor))
                {
                    e.Graphics.FillRectangle(brush, 10, 10, rectWidth, rectHeight);
                }
            }
        }

        public Form1()
        {
            InitializeComponent();
            paintToolStripMenuItem.Enabled = false;
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }
        private void quitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void paintToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (canPaint)
            {
                if (rectWidth > this.ClientSize.Width || rectHeight > this.ClientSize.Height)
                {
                    MessageBox.Show("The rectangle size exceeds the window size.");
                    return;
                }

                // Vẽ hình chữ nhật
                this.Invalidate(); // Yêu cầu vẽ lại Form
            }
            else
            {
                MessageBox.Show("Please set the size and color before painting.");
            }
        }

        private void colorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (ColorDialog colorDialog = new ColorDialog())
            {
                if (colorDialog.ShowDialog() == DialogResult.OK)
                {
                    rectColor = colorDialog.Color;

                    if (canPaint)
                    {
                        this.Invalidate(); // Vẽ lại Form để áp dụng màu mới
                    }
                }
            }
        }
        private void sizeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SizeColorForm sizeForm = new SizeColorForm();
            if (sizeForm.ShowDialog() == DialogResult.OK)
            {
                // Lấy giá trị kích thước và màu sắc từ SizeColorForm
                rectWidth = sizeForm.RectangleWidth;
                rectHeight = sizeForm.RectangleHeight;
                rectColor = sizeForm.SelectedColor;

                // Bật chức năng Paint
                canPaint = true;
                paintToolStripMenuItem.Enabled = true; // Bật tùy chọn Paint trong menu
            }
        }
    }
}