INMEST Management
This contains models for an LMS including Courses, Class Schedules, Attendance, Queries etc.

## Models
### Course
- Represents a course offering
- Fields for name, description, creation/modified dates

### ClassSchedule
- Represents scheduled class sessions
- Title, description, start/end times, frequency etc.
- Links to Cohort model via ForeignKey

### ClassAttendance
- Records attendance at scheduled classes
- Links to ClassSchedule and User (Attendee)
- Marks if user was present
### Query

- Supports questions/queries raised by users
- Has title, description, status fields
- Links to user who submitted and user assigned to query

### QueryComment
- Stores comments against queries
- Links to parent Query and commenting User

### Features
- Manage course catalog and scheduling
- Track class attendance
- User query ticketing and resolution
- Comments on queries

### Usage
Key examples:

- Admins can create courses and schedules
- Users can view schedules and mark attendance
- Users can submit queries which get assigned
- Queries can be commented on until resolved