from bokeh.layouts import column
from bokeh.models import DataTable, TableColumn, ColumnDataSource, TextInput, CustomJS
from bokeh.plotting import output_file, save
import pandas as pd

# Sample data
data = {
    'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson', 'Emma Davis', 
             'Frank Miller', 'Grace Lee', 'Henry Taylor', 'Iris Anderson', 'Jack Thomas'],
    'Department': ['Sales', 'Marketing', 'IT', 'Sales', 'HR', 
                   'IT', 'Marketing', 'Sales', 'HR', 'IT'],
    'Position': ['Manager', 'Analyst', 'Developer', 'Representative', 'Coordinator',
                 'Engineer', 'Specialist', 'Manager', 'Director', 'Developer'],
    'Salary': [75000, 55000, 68000, 45000, 52000, 
               72000, 58000, 80000, 95000, 65000]
}

df = pd.DataFrame(data)

# Create ColumnDataSource with both original and filtered data
source = ColumnDataSource(df)
source_original = ColumnDataSource(df)

# Create columns for the table
columns = [
    TableColumn(field="Name", title="Name"),
    TableColumn(field="Department", title="Department"),
    TableColumn(field="Position", title="Position"),
    TableColumn(field="Salary", title="Salary"),
]

# Create DataTable
data_table = DataTable(source=source, columns=columns, width=800, height=400, 
                       editable=False, selectable=True)

# Create TextInput for filtering
filter_input = TextInput(value="", title="Filter (searches all columns):", 
                         placeholder="Type to filter...", width=800)

# JavaScript callback for dynamic filtering
callback = CustomJS(args=dict(source=source, source_original=source_original, filter_input=filter_input), 
                    code="""
    const data = source.data;
    const original_data = source_original.data;
    const filter_value = filter_input.value.toLowerCase();
    
    // Get all column names
    const columns = Object.keys(original_data);
    
    // If filter is empty, show all data
    if (filter_value === '') {
        for (let key of columns) {
            data[key] = original_data[key].slice();
        }
        source.change.emit();
        return;
    }
    
    // Find matching rows
    const num_rows = original_data[columns[0]].length;
    const matching_indices = [];
    
    for (let i = 0; i < num_rows; i++) {
        let row_matches = false;
        
        // Check if any column in this row matches the filter
        for (let col of columns) {
            const cell_value = String(original_data[col][i]).toLowerCase();
            if (cell_value.includes(filter_value)) {
                row_matches = true;
                break;
            }
        }
        
        if (row_matches) {
            matching_indices.push(i);
        }
    }
    
    // Update source data with filtered rows
    for (let key of columns) {
        data[key] = matching_indices.map(i => original_data[key][i]);
    }
    
    source.change.emit();
""")

# Attach callback to filter input
filter_input.js_on_change('value', callback)

# Create layout
layout = column(filter_input, data_table)

output_file("output/interactive_charts_05.html")
save(layout)