# 900 - Entity-Relationship Diagram (ERD)

``` mermaid
erDiagram
    Board ||--|{ Field : "board has one or more fields"
    Camera }|--|| CameraType : "camera has one type"
    CameraType
    Character }|--|| CharacterRole : "character has one role"
    CharacterRole
    Field }|--|| FieldType : "field has one type"
    Field
    FieldType
    Game }|--|| Board : "game has one board"
    Light
    Player
    PlayerRole
    Prop
    Scene
    Shot
    Tag
    User
    UserRole
```
