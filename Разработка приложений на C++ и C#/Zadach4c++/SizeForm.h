#pragma once
namespace Zadach4c {
	using namespace System;
	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;
	public ref class SizeForm : public System::Windows::Forms::Form
	{
	public:
		SizeForm(void)
		{
			InitializeComponent();
		}

	protected:

		~SizeForm()
		{
			if (components)
			{
				delete components;
			}
		}
	private: System::Windows::Forms::Label^ label1;
	protected:
	private: System::Windows::Forms::Label^ label2;
	private: System::Windows::Forms::TextBox^ textBox1;
	private: System::Windows::Forms::TextBox^ textBox2;
	private: System::Windows::Forms::Label^ label3;
	private: System::Windows::Forms::CheckBox^ checkBox1;
	private: System::Windows::Forms::CheckBox^ checkBox2;
	private: System::Windows::Forms::CheckBox^ checkBox3;
	private: System::Windows::Forms::Button^ button1;

	private:
		System::ComponentModel::Container^ components;

#pragma region Windows Form Designer generated code

		void InitializeComponent(void)
		{
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->textBox1 = (gcnew System::Windows::Forms::TextBox());
			this->textBox2 = (gcnew System::Windows::Forms::TextBox());
			this->label3 = (gcnew System::Windows::Forms::Label());
			this->checkBox1 = (gcnew System::Windows::Forms::CheckBox());
			this->checkBox2 = (gcnew System::Windows::Forms::CheckBox());
			this->checkBox3 = (gcnew System::Windows::Forms::CheckBox());
			this->button1 = (gcnew System::Windows::Forms::Button());
			this->SuspendLayout();
			// 
			// label1
			// 
			this->label1->AutoSize = true;
			this->label1->Location = System::Drawing::Point(202, 44);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(52, 16);
			this->label1->TabIndex = 0;
			this->label1->Text = L"WIDTH";
			// 
			// label2
			// 
			this->label2->AutoSize = true;
			this->label2->Location = System::Drawing::Point(202, 124);
			this->label2->Name = L"label2";
			this->label2->Size = System::Drawing::Size(58, 16);
			this->label2->TabIndex = 1;
			this->label2->Text = L"HEIGHT";
			// 
			// textBox1
			// 
			this->textBox1->Location = System::Drawing::Point(327, 38);
			this->textBox1->Name = L"textBox1";
			this->textBox1->Size = System::Drawing::Size(100, 22);
			this->textBox1->TabIndex = 2;
			this->textBox1->Text = L"0";
			// 
			// textBox2
			// 
			this->textBox2->Location = System::Drawing::Point(327, 118);
			this->textBox2->Name = L"textBox2";
			this->textBox2->Size = System::Drawing::Size(100, 22);
			this->textBox2->TabIndex = 3;
			this->textBox2->Text = L"0";
			// 
			// label3
			// 
			this->label3->AutoSize = true;
			this->label3->Location = System::Drawing::Point(369, 230);
			this->label3->Name = L"label3";
			this->label3->Size = System::Drawing::Size(39, 16);
			this->label3->TabIndex = 4;
			this->label3->Text = L"Color";
			// 
			// checkBox1
			// 
			this->checkBox1->AutoSize = true;
			this->checkBox1->Location = System::Drawing::Point(154, 314);
			this->checkBox1->Name = L"checkBox1";
			this->checkBox1->Size = System::Drawing::Size(58, 20);
			this->checkBox1->TabIndex = 5;
			this->checkBox1->Text = L"RED";
			this->checkBox1->UseVisualStyleBackColor = true;
			// 
			// checkBox2
			// 
			this->checkBox2->AutoSize = true;
			this->checkBox2->Location = System::Drawing::Point(350, 314);
			this->checkBox2->Name = L"checkBox2";
			this->checkBox2->Size = System::Drawing::Size(77, 20);
			this->checkBox2->TabIndex = 6;
			this->checkBox2->Text = L"GREEN";
			this->checkBox2->UseVisualStyleBackColor = true;
			// 
			// checkBox3
			// 
			this->checkBox3->AutoSize = true;
			this->checkBox3->Location = System::Drawing::Point(544, 314);
			this->checkBox3->Name = L"checkBox3";
			this->checkBox3->Size = System::Drawing::Size(64, 20);
			this->checkBox3->TabIndex = 7;
			this->checkBox3->Text = L"BLUE";
			this->checkBox3->UseVisualStyleBackColor = true;
			// 
			// button1
			// 
			this->button1->Location = System::Drawing::Point(352, 408);
			this->button1->Name = L"button1";
			this->button1->Size = System::Drawing::Size(75, 23);
			this->button1->TabIndex = 8;
			this->button1->Text = L"OK";
			this->button1->UseVisualStyleBackColor = true;
			this->button1->Click += gcnew System::EventHandler(this, &SizeForm::button1_Click);
			// 
			// SizeForm
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(8, 16);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->ClientSize = System::Drawing::Size(793, 517);
			this->Controls->Add(this->button1);
			this->Controls->Add(this->checkBox3);
			this->Controls->Add(this->checkBox2);
			this->Controls->Add(this->checkBox1);
			this->Controls->Add(this->label3);
			this->Controls->Add(this->textBox2);
			this->Controls->Add(this->textBox1);
			this->Controls->Add(this->label2);
			this->Controls->Add(this->label1);
			this->Name = L"SizeForm";
			this->Text = L"SizeForm";
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion
	public:
		int GetWidth() { return int::Parse(textBox1->Text); }
		int GetHeight() { return int::Parse(textBox2->Text); }
		Color GetSelectedColor() {
			if (checkBox1->Checked) return Color::Red;
			if (checkBox2->Checked) return Color::Green;
			if (checkBox3->Checked) return Color::Blue;
			return Color::Black; //Цвет по умолчанию, если ни один из них не выбран
		}

	private: System::Void button1_Click(System::Object^ sender, System::EventArgs^ e) {
		try {
			int width = GetWidth();
			int height = GetHeight();
			if (width <= 0 || height <= 0) {
				MessageBox::Show("Пожалуйста, введите правильные целые положительные числа для ширины и высоты.", "Invalid Input", MessageBoxButtons::OK, MessageBoxIcon::Error);
				return;
			}
			this->DialogResult = System::Windows::Forms::DialogResult::OK;
			this->Close();
		}
		catch (Exception^ ex) {
			MessageBox::Show("Введите правильные числовые значения для ширины и высоты.", "Invalid Input", MessageBoxButtons::OK, MessageBoxIcon::Error);
		}
	}
	};
}