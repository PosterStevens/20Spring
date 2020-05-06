#include <iostream>
#include <fstream> 
#include <string.h>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

// split line into vector of strings
vector<string> split_line(const string&, const string&);
// convert a sequence of string to n-gram, then write n-gram into csv file
vector<vector<string>> to_n_gram(vector<string>&, int n, ofstream& outfile);
// write n-gram into file
void write_into_file(ofstream&, vector<string>);


// Input: window_size, input_filename, *featureNames
int main(int argc, char* argv[]) {
	ifstream infile; // infile object used to read data
	ofstream outfile; // final output file
	string line; // each line read from input file
	unordered_map<string, int> dict; // define a map, mapping column name into column index
	vector<string> desired_attr; // the features that we want to use to create n-gram; for example, sku_Id, 
	vector<string> sequence_data; // a sentence of item
	int window_size = stoi(argv[1]); // windows size, a windows size of 2 indicates a 5-gram
	//cout << "please specify window size > "; cin >> window_size;
	string filename = argv[2];
	string outfilename = argv[3];
	// receive argument from command line
	for (int i = 4; argv[i] != NULL; ++i) desired_attr.push_back(argv[i]); 
	
	// open input file, open output file
	infile.open(filename);
	outfile.open("n_grams.csv");

	// read the first line: the header line
	// split the header line
	// define column name to column index map
	getline(infile, line);	
	vector<string> header = split_line(line, ",");
	for (int i = 0; i < header.size(); i++) dict[header[i]] = i;

	
	// loop over all the line in input file
	// if the userId this line is equal to the userId of the previous line, 
	// then add line into sequence
	// if it's not equal, convert sequence into n-gram, then write into output file

	string userId = ""; // initiate userId as null
	int userIdCol = dict["user_Id"]; // use name2index map to get index of user_Id column
	int j = 0;
	while (getline(infile, line)) {
		vector<string> data_line = split_line(line, ",");
		//cout << (data_line[userIdCol] == userId) << endl; 
		if (data_line[userIdCol] != userId){
			userId = data_line[userIdCol];
			if (j == 0) j+=1; else to_n_gram(sequence_data, window_size, outfile);
			sequence_data.clear();
			//continue;
		}

		int j = 0;
		string data = "";
		for (string attr: desired_attr){
			int col = dict[attr];
			data += data_line[col];
			data += "_";
		}
		sequence_data.push_back(data);// for (string data: sequence_data) cout << data << ","; cout << endl;
	} 
	
	outfile.close();
	infile.close();
	return 0;
}

// split line into vector of string
vector<string> split_line(const string& line, const string& delimeter){
	vector<string> output;
	if ("" == line) return output; // if the line is null, return empty vector
	char * strs = new char[line.length()+1]; // convert string into char[]
	strcpy(strs, line.c_str()); // copy content in string to char

	char * d = new char[delimeter.length()+1]; // convert string into char[]
	strcpy(d, delimeter.c_str()); // copy content in string to char

	char * p = strtok(strs, d);

	while (p) {
		string s = p;
		output.push_back(s);
		p = strtok(NULL, d); 
	}
	free(strs); free(d);
	return output;
}


vector<vector<string>> to_n_gram(vector<string>& sequence, int n, ofstream& outfile){
	vector<vector<string>> output;

	for (int i = 0; i < sequence.size(); ++i){
		vector<string> n_gram;
		for (int j = -n; j <= n; ++j){
			if (((i + j) < 0) || (i + j) >= sequence.size()){
				n_gram.push_back("NONE");
			}
			else{
				n_gram.push_back(sequence[i+j]);
			}
		}
		output.push_back(n_gram);
		write_into_file(outfile, n_gram);
	}

	return output;
}


void write_into_file(ofstream& outfile, vector<string> n_gram){
	for (int i = 0; i < n_gram.size()-1; ++i){
		outfile << n_gram[i] << ",";
	}
	outfile << n_gram[n_gram.size()-1] << endl;
}