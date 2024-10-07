# 900 - Entity-Relationship Diagram (ERD)

``` mermaid
erDiagram
    Story ||--o{ Game : "story has zero or more games"
    Game }|--|| Board : "game has one board"
    Board ||--|{ Field : "board has one or more fields"
    Camera }|--|| CameraType : "camera has one type"
    Character }|--|| CharacterRole : "character has one role"
    Field }|--|| FieldType : "field has one type"
    Game ||--o{ Player : "game has zero or more players"
    Light }|--|| LightType : "light has one type"
    Player }|--|| PlayerRole : "player has one role"
    Player }|--|| User : "player has one user"  
    Player }|--|| Character : "player has one character"  
    Story ||--o{ Screenplay : "story has zero or more screenplays"
    Screenplay ||--o{ Scene : "screenplay has zero or more scenes"
    Scene ||--o{ Character : "scene has zero or more characters"
    Scene ||--o{ Camera : "scene has zero or more cameras"
    Scene ||--o{ Light : "scene has zero or more lights"
    Scene ||--o{ Prop : "scene has zero or more props"
    Scene ||--o{ Shot : "scene has zero or more shots"    
    Scene ||--o{ Tag : "scene has zero or more tags"
    User }|--|| UserRole : "user has one role"
```
