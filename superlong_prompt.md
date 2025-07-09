# Grade Calculation System - Detailed Requirements

## 1. Project Overview
Create a robust grade calculation system that processes student exam responses and calculates final grades based on correct answers.

## 2. Input Data Requirements
- **Student Information**: Include student names and IDs
- **Raw Answer Data**: Student responses to multiple-choice questions (A, B, C, D format)
- **Answer Key**: Correct answers for comparison
- **Question Count**: Total number of questions in the exam

## 3. Data Structure Specifications
- Use JSON format for structured data storage
- Include the following fields for each student:
  - `student_id`: Unique identifier (string)
  - `student_name`: Full name (string)
  - `answers`: Array of student responses (array of strings)
- Include a separate answer key array with correct responses

## 4. Processing Requirements
- **Input Validation**: 
  - Verify all students have answered all questions
  - Check that answers are valid (A, B, C, or D only)
  - Ensure student data is complete and properly formatted
- **Grade Calculation Logic**:
  - Calculate raw score (number of correct answers)
  - Convert to percentage: (correct_answers / total_questions) × 100
  - Apply grading scale:
    - A: 90-100%
    - B: 80-89%
    - C: 70-79%
    - D: 60-69%
    - F: Below 60%

## 5. Output Requirements
- Display results for each student including:
  - Student name and ID
  - Raw score (e.g., "8/10")
  - Percentage score
  - Letter grade
- Generate summary statistics:
  - Class average
  - Highest and lowest scores
  - Grade distribution

## 6. Error Handling
- Handle missing or invalid student data gracefully
- Provide clear error messages for invalid inputs
- Continue processing valid data even if some entries are invalid

## 7. Code Quality Requirements
- Use meaningful variable names
- Include proper comments explaining logic
- Implement functions for reusable code blocks
- Follow consistent coding style
- Include type hints where applicable

## 8. Testing Requirements
- Test with various score ranges (high, medium, low)
- Test edge cases (perfect scores, zero scores)
- Verify error handling with invalid inputs
- Test with different class sizes

## 9. Output Format
Save results to a text file with clear formatting and readable layout. 