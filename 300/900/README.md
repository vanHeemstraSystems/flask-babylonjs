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
    Player
    PlayerRole
    Prop
    Scene
    Shot
    Tag
    User ||--o{ Player : "user has zero or more players"
    User }|--|| UserRole : "user has one role"
    UserRole
```
