# hw-06b: Triangle Classification Testing

**Course:** SSW 567 - Software Testing, Quality Assurance and Maintenance
**Institution:** Stevens Institute of Technology
**Assignment:** Triangle Classification Testing and Debugging

---

## Assignment Overview

This repository contains a comprehensive triangle classification testing project that demonstrates:
- Systematic test case development using equivalence partitioning and boundary value analysis
- Code inspection and quality improvement
- Formal test reporting
- Version control with Git

---

## Repository Contents

### Core Files
- **Triangle.py** - Triangle classification implementation with classify_triangle() function
- **TestTriangle.py** - Comprehensive test suite with 35 test cases

### Test Reports
- **TestReport1.md** - Initial testing of original implementation (35/35 tests passed)
- **TestReport2.md** - Final testing of improved implementation (35/35 tests passed)
- **CodeInspectionReport.md** - Detailed code analysis documentation

### Test Outputs
- **test_run1_output.txt** - Part 1 test execution output
- **test_run2_output.txt** - Part 2 test execution output

### Documentation
- **ASSIGNMENT_SUMMARY.md** - Complete assignment summary with all deliverables
- **README.md** - This file

---

## How to Run

### Run All Tests
```bash
python -m unittest TestTriangle -v
```

### Run Directly
```bash
python TestTriangle.py
```

### Run Triangle Examples
```bash
python Triangle.py
```

---

## Test Results Summary

| Metric | Part 1 (Original) | Part 2 (Improved) |
|--------|-------------------|-------------------|
| Tests Planned | 35 | 35 |
| Tests Executed | 35 | 35 |
| Tests Passed | 35 | 35 |
| Tests Failed | 0 | 0 |
| Pass Rate | 100% | 100% |
| Defects Found | 0 | 0 |
| Code Improvements | 0 | 1 |

---

## Test Suite Coverage

The 35 comprehensive test cases cover:

### Valid Triangles (16 tests)
- **Equilateral** (3 tests): Small, medium, large triangles
- **Isosceles** (6 tests): All pair combinations, various sizes
- **Scalene** (3 tests): Small, medium, large triangles
- **Right Triangles** (6 tests): Multiple Pythagorean triples, isosceles right

### Invalid Triangles (17 tests)
- **Triangle Inequality Violations** (4 tests)
- **Zero Values** (4 tests)
- **Negative Values** (4 tests)
- **Boundary Cases** (3 tests)
- **Edge Cases** (2 tests)

### Special Cases (2 tests)
- **Floating Point Values** (2 tests)

---

## Project Timeline

### Part 0: Repository Setup ✅
- Created GitHub repository
- Committed original Triangle.py and TestTriangle.py

### Part 1: Test Suite Enhancement ✅
- Expanded from 6 to 35 test cases
- Applied equivalence partitioning and boundary value analysis
- Executed tests: 35/35 passed
- Created TestReport1.md

### Part 2: Code Improvement ✅
- Performed code inspection
- Fixed code organization issue
- Re-executed tests: 35/35 passed
- Created TestReport2.md and CodeInspectionReport.md

---

## Key Findings

1. **Original Implementation Quality**: The classify_triangle() function was correctly implemented with no functional defects

2. **Code Improvement**: Fixed code organization issue (file writing at module level)

3. **Test Coverage**: 35 strategic test cases provide comprehensive coverage

4. **No Regressions**: All improvements maintained 100% test pass rate

---

## Testing Strategy

**Equivalence Partitioning:**
- Valid triangles: Equilateral, Isosceles, Scalene, Right
- Invalid triangles: Negative, zero, inequality violations

**Boundary Value Analysis:**
- Minimum values (1,1,1)
- Large values (100,150,200)
- Degenerate cases (sum equals side)

**Combination Testing:**
- All pair combinations for isosceles
- Different parameter orders
- All positions for invalid values

---

## Git History

```
commit 3: Part 2 - Code quality improvement and final testing
commit 2: Part 1 - Enhanced test suite with 35 comprehensive test cases
commit 1: Part 0 - Initial commit with original triangle code
```

---

## Technologies Used

- **Language:** Python 3.x
- **Testing Framework:** unittest (Python standard library)
- **Version Control:** Git
- **Repository Hosting:** GitHub

---

## Assignment Completion Status

- ✅ Part 0: Repository setup and initial commit
- ✅ Part 1: Test suite enhancement and Test Report 1
- ✅ Part 2: Code improvement and Test Report 2
- ✅ Complete documentation and assignment summary

**Status:** 🎉 COMPLETE - All requirements met with 100% test pass rate

---

## Contact

For questions about this assignment, please contact the course instructor.

---

## License

This is an academic project for SSW 567 at Stevens Institute of Technology.
