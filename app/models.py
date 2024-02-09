from sqlalchemy import( 
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Date, 
    Text
)

# from sqlalchemy.orm import relationship

from .database import Base

'''
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
'''




class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    type = Column(String, index=True)
    date = Column(Date)
    description = Column(Text)
    drive = Column(String)
    thumbnail = Column(String)



class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)

class EventTeam(Base):
    __tablename__ = "event_teams"

    id_event = Column(Integer, ForeignKey("events.id"), primary_key=True)
    id_team = Column(Integer, ForeignKey("teams.id"), primary_key=True)

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    linkedin = Column(String)
    is_public = Column(Boolean, default=True)
    password = Column(String, nullable=False)


class ParticipantTeam(Base):
    __tablename__ = "participant_teams"

    id_team = Column(Integer, ForeignKey("teams.id"), primary_key=True)
    id_participant = Column(Integer, ForeignKey("participants.id"), primary_key=True)

class Mentor(Base):
    __tablename__ = "mentors"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    role = Column(String)
    password = Column(String, nullable=False)


class EventMentor(Base):
    __tablename__ = "event_mentors"

    id_event = Column(Integer, ForeignKey("events.id"), primary_key=True)
    id_mentor = Column(Integer, ForeignKey("mentors.id"), primary_key=True)

class Speaker(Base):
    __tablename__ = "speakers"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    password = Column(String, nullable=False)


class EventSpeaker(Base):
    __tablename__ = "event_speakers"

    id_event = Column(Integer, ForeignKey("events.id"), primary_key=True)
    id_speaker = Column(Integer, ForeignKey("speakers.id"), primary_key=True)

class Field(Base):
    __tablename__ = "fields"

    name = Column(String, primary_key=True)

class Criteria(Base):
    __tablename__ = "criteria"

    name = Column(String, primary_key=True)
    name_field = Column(String, ForeignKey("fields.name"))

class EventCriteria(Base):
    __tablename__ = "event_criteria"

    id_event = Column(Integer, ForeignKey("events.id"), primary_key=True)
    name_criteria = Column(String, ForeignKey("criteria.name"))
    score = Column(Integer) # out of 20 

class EventSubmission(Base):
    __tablename__ = "event_submissions"

    id_event = Column(Integer, ForeignKey("events.id"), primary_key=True)
    id_team = Column(Integer, ForeignKey("teams.id"), primary_key=True)
    id_field = Column(String, ForeignKey("fields.name"), primary_key=True)
    submission = Column(Text)

class Judge(Base):
    __tablename__ = "judges"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    password = Column(String, nullable=False)

class EventJudge(Base):
    __tablename__ = "event_judges"

    id_judge = Column(Integer, ForeignKey("judges.id"), primary_key=True)
    id_event = Column(Integer, ForeignKey("events.id"), primary_key=True)
    id_team = Column(Integer, ForeignKey("teams.id"), primary_key=True)
    name_criteria = Column(String, ForeignKey("criteria.name"), primary_key=True)
    judgment = Column(Text)
    role = Column(String)

class LostObject(Base):
    __tablename__ = "lost_objects"

    img_link = Column(Integer, primary_key=True)
    id_event = Column(Integer, ForeignKey("events.id"))
    status = Column(Boolean, default=False)  # False  === not found yet