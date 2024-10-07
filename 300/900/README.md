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
    Player }|--|| Character : "player has one character"
    Player }|--|| PlayerRole : "player has one role"
    Player }|--|| User : "player has one user"    
    PlayerRole
    Prop
    Scene ||--o{ Camera : "scene has zero or more cameras"
    Scene ||--o{ Character : "scene has zero or more characters"
    Scene ||--o{ Light : "scene has zero or more lights"
    Scene ||--o{ Prop : "scene has zero or more props"
    Scene ||--o{ Shot : "scene has zero or more shots"    
    Scene ||--o{ Tag : "scene has zero or more tags"
    Shot
    Tag
    User }|--|| UserRole : "user has one role"
    UserRole
```
