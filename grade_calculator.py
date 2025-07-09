#!/usr/bin/env python3
"""
Grade Calculator Script
Processes student exam data and calculates grades based on correct answers.
"""

import json
import sys
from typing import Dict, List, Tuple, Any


def load_exam_data(filename: str) -> Dict[str, Any]:
    """
    Load exam data from JSON file with error handling.
    
    Args:
        filename: Path to the JSON file containing exam data
        
    Returns:
        Dictionary containing exam data
        
    Raises:
        FileNotFoundError: If the data file doesn't exist
        json.JSONDecodeError: If the JSON is malformed
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find data file '{filename}'")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{filename}': {e}")
        sys.exit(1)


def validate_student_data(student: Dict[str, Any], total_questions: int) -> Tuple[bool, str]:
    """
    Validate individual student data for completeness and correctness.
    
    Args:
        student: Dictionary containing student information
        total_questions: Expected number of questions
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check required fields
    required_fields = ['student_id', 'student_name', 'answers']
    for field in required_fields:
        if field not in student:
            return False, f"Missing required field: {field}"
    
    # Check answer count
    if len(student['answers']) != total_questions:
        return False, f"Expected {total_questions} answers, got {len(student['answers'])}"
    
    # Validate answer format
    valid_answers = {'A', 'B', 'C', 'D'}
    for i, answer in enumerate(student['answers']):
        if answer not in valid_answers:
            return False, f"Invalid answer '{answer}' at question {i+1}"
    
    return True, ""


def calculate_grade(student_answers: List[str], answer_key: List[str]) -> Tuple[int, float, str]:
    """
    Calculate student grade based on correct answers.
    
    Args:
        student_answers: List of student's answers
        answer_key: List of correct answers
        
    Returns:
        Tuple of (correct_count, percentage, letter_grade)
    """
    correct_count = sum(1 for student_ans, correct_ans in zip(student_answers, answer_key) 
                       if student_ans == correct_ans)
    
    percentage = (correct_count / len(answer_key)) * 100
    
    # Determine letter grade
    if percentage >= 90:
        letter_grade = 'A'
    elif percentage >= 80:
        letter_grade = 'B'
    elif percentage >= 70:
        letter_grade = 'C'
    elif percentage >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    return correct_count, percentage, letter_grade


def generate_summary_stats(grades_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate summary statistics for the class.
    
    Args:
        grades_data: List of grade dictionaries for each student
        
    Returns:
        Dictionary containing summary statistics
    """
    percentages = [grade['percentage'] for grade in grades_data]
    letter_grades = [grade['letter_grade'] for grade in grades_data]
    
    stats = {
        'class_average': sum(percentages) / len(percentages),
        'highest_score': max(percentages),
        'lowest_score': min(percentages),
        'grade_distribution': {}
    }
    
    # Calculate grade distribution
    for grade in ['A', 'B', 'C', 'D', 'F']:
        stats['grade_distribution'][grade] = letter_grades.count(grade)
    
    return stats


def process_grades(limit_students: int = None) -> str:
    """
    Main processing function that handles the complete grading workflow.
    
    Args:
        limit_students: Optional limit on number of students to process
        
    Returns:
        Formatted output string with all results
    """
    # Load data
    data = load_exam_data('exam_data.json')
    
    exam_info = data['exam_info']
    answer_key = data['answer_key']
    students = data['students']
    
    if limit_students:
        students = students[:limit_students]
    
    total_questions = exam_info['total_questions']
    output_lines = []
    
    # Header
    output_lines.extend([
        "=" * 60,
        f"EXAM RESULTS: {exam_info['exam_name']}",
        f"Date: {exam_info['date']}",
        f"Total Questions: {total_questions}",
        "=" * 60,
        ""
    ])
    
    # Process each student
    grades_data = []
    processed_count = 0
    
    for student in students:
        # Validate student data
        is_valid, error_msg = validate_student_data(student, total_questions)
        
        if not is_valid:
            output_lines.append(f"⚠️  ERROR processing {student.get('student_name', 'Unknown')}: {error_msg}")
            continue
        
        # Calculate grade
        correct_count, percentage, letter_grade = calculate_grade(
            student['answers'], answer_key
        )
        
        # Store grade data for statistics
        grade_data = {
            'student_name': student['student_name'],
            'percentage': percentage,
            'letter_grade': letter_grade,
            'correct_count': correct_count
        }
        grades_data.append(grade_data)
        
        # Format individual result
        output_lines.extend([
            f"Student: {student['student_name']} (ID: {student['student_id']})",
            f"Score: {correct_count}/{total_questions} ({percentage:.1f}%)",
            f"Grade: {letter_grade}",
            "-" * 40
        ])
        
        processed_count += 1
    
    # Generate summary statistics
    if grades_data:
        output_lines.append("\nCLASS SUMMARY STATISTICS")
        output_lines.append("=" * 30)
        
        stats = generate_summary_stats(grades_data)
        
        output_lines.extend([
            f"Students Processed: {processed_count}",
            f"Class Average: {stats['class_average']:.1f}%",
            f"Highest Score: {stats['highest_score']:.1f}%",
            f"Lowest Score: {stats['lowest_score']:.1f}%",
            "",
            "Grade Distribution:"
        ])
        
        for grade, count in stats['grade_distribution'].items():
            if count > 0:
                output_lines.append(f"  {grade}: {count} student(s)")
    
    else:
        output_lines.append("⚠️  No valid student data was processed.")
    
    return "\n".join(output_lines)


def main():
    """Main execution function."""
    print("Processing grades for 3 students...")
    
    try:
        # Process grades for first 3 students as requested
        result = process_grades(limit_students=3)
        
        # Save to output file
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(result)
        
        print("✅ Grade processing completed successfully!")
        print("📄 Results saved to 'output.txt'")
        
        # Also display results to console
        print("\nResults Preview:")
        print("-" * 50)
        print(result)
        
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 