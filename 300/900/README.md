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
    Light }|--|| LightType : "light has one type"
    LightType
    Player }|--|| User : "player has one user"
    Player }|--|| Character : "player has one character"
    Player }|--|| PlayerRole : "player has one role"
    PlayerRole
    Prop
    Scene O{--|{ Prop : "scene has zero or more props"
    Scene O{--|{ Light : "scene has zero or more lights"
    Scene O{--|{ Character : "scene has zero or more characters"
    Scene O{--|{ Tag : "scene has zero or more tags"
    Shot
    Tag
    User }|--|| UserRole : "user has one role"
    UserRole
```
