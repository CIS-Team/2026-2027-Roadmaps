# Level 2: Intermediate

[Back to overview](../README.md) · Previous: [Beginner](../01-beginner/README.md)

**Goal:** build more complete games using the tools and techniques used in real projects: clean code architecture, saving, cameras, level tools, UI, game feel, AI movement, lighting, shaders and optimization. This level is for members who finished the beginner track, or who already know the basics of Unity and C#. It takes 12 weeks at 4-5 hours per week.

Most tasks are the same: apply the topic to a game you already made, or to a new one. Over the 12 weeks your projects get better, and they become your portfolio.

Resources marked **optional**, **advanced** or **reference** are not required. Use them when you need them.

## Learning Path

| Week | Topic | Outcome |
|:--:|:--|:--|
| **1** | [OOP and advanced techniques](#week-1-oop-and-advanced-techniques) | Cleaner, better organized code in a project |
| **2** | [New input system and the animator](#week-2-new-input-system-and-the-animator) | New input system and blend trees in your projects |
| **3** | [Save systems](#week-3-save-systems) | A working save system |
| **4** | [Cinemachine, tilemaps, terrain and ProBuilder](#week-4-cinemachine-tilemaps-terrain-and-probuilder) | Cameras and level tools used in a project |
| **5** | [ScriptableObjects](#week-5-scriptableobjects) | Data and events built on ScriptableObjects |
| **6** | [UI and DOTween](#week-6-ui-and-dotween) | Advanced, animated UI |
| **7** | [Design patterns and architecture](#week-7-design-patterns-and-architecture) | Design patterns applied to a project |
| **8** | [Game feel and juice](#week-8-game-feel-and-juice) | A polished game |
| **9** | [NavMesh](#week-9-navmesh) | Characters that navigate the world |
| **10** | [Lighting and post-processing](#week-10-lighting-and-post-processing) | A lit scene with post-processing |
| **11** | [Shaders](#week-11-shaders) | A shader of your own |
| **12** | [Profiling and optimization](#week-12-profiling-and-optimization) | A measured performance improvement |

------------------------------------------------------------------------

## Week 1: OOP and advanced techniques

| Resources | Learning Objectives |
|:--|:--|
| [ِAdvanced Techniques](https://youtu.be/mdyeJpW3bcU) <br> [Applying the Advanced Techniques](https://youtu.be/lx5sL_7actg) | Object-oriented programming in C# and more advanced coding techniques for Unity projects. |

**Task:** Apply what you learned to an old game or a new one.

## Week 2: New input system and the animator

| Topic | Resources | Learning Objectives |
|:--|:--|:--|
| **New input system** | [New input system guide](https://youtu.be/1b7H203kBVg) | Set up input actions and bindings, and replace the old input system. |
| **Animator** | [Animator playlist](https://www.youtube.com/playlist?list=PLwyUzJb_FNeTQwyGujWRLqnfKpV-cj-eO) | Animator controllers, states and transitions, parameters, and blend trees. |

**Task:** Convert the old input system to the new one in your projects. Use advanced animator techniques such as blend trees.

## Week 3: Save systems

| Resources | Learning Objectives |
|:--|:--|
| [Save system playlist](https://www.youtube.com/playlist?list=PL3viUl9h9k7-tMGkSApPdu4hlUBagKial) | Design and build a system that saves and loads game data between sessions. |

**Task:** Create a save system.

## Week 4: Cinemachine, tilemaps, terrain and ProBuilder

| Topic | Resources | Learning Objectives |
|:--|:--|:--|
| **Cinemachine** | [Cinemachine playlist](https://www.youtube.com/playlist?list=PLX2vGYjWbI0QiMBrmyzbxZeHepAbhVOJa) | Virtual cameras, following targets, and camera transitions. |
| **Terrain** | [Beginner guide to terrain](https://youtu.be/HXvC9pFHWvM) <br> [Full terrain beginner playlist](https://www.youtube.com/playlist?list=PLS7jk2aVN8G4gjIPTeyVhK0HYEbVY7xSa) <br> *Optional, advanced:* [Rendering on terrains](https://www.youtube.com/playlist?list=PLbT_kxJXjbqIcRrbrr3BchV2B1jPQu3CP) | Sculpt and texture terrain, and build 3D landscapes. The advanced playlist covers how terrain is rendered. |
| **Tilemaps** | [Beginner guide to tilemaps](https://youtu.be/4x4d2V7SjC8) <br> *Advanced:* [Data and dynamic tiles](https://www.youtube.com/playlist?list=PLeFyPLcO7nx9de3UX0omn_IfgAtCXjpWs) <br> *Reference:* [Collection of tilemap resources](https://www.youtube.com/playlist?list=PLGYLjm4eD1gBRp9rxviFZJUfRndFa_vdf) | Build 2D levels with tilemaps. The advanced playlist covers tile data and dynamic tiles. |
| **ProBuilder** | [Master ProBuilder in Unity 6](https://www.youtube.com/watch?v=Bfl-V-39JlU) | Build and prototype 3D levels with Unity's built-in modeling tools. |

**Task:** Use Cinemachine, tilemaps and terrain in your projects.

## Week 5: ScriptableObjects

| Resources | Learning Objectives |
|:--|:--|
| [Ryan Hipple's talk](https://youtu.be/raQ3iHhE_Kk) <br> [SOAP](https://youtu.be/bO8WOHCxPq8) <br> [Event channels, part 1](https://youtu.be/h8ZAOWY_5LA) <br> [Event channels, part 2](https://youtu.be/95eFgUENnTc) | Use ScriptableObjects to store data and to connect systems with event channels, so parts of your game do not depend on each other directly. |

**Task:** Use ScriptableObjects in a project: for data, for event channels, and for other things where they fit.

## Week 6: UI and DOTween

| Topic | Resources | Learning Objectives |
|:--|:--|:--|
| **DOTween** | [DOTween easy playlist](https://www.youtube.com/playlist?list=PLTBYgwZphpgZWgsSX4eQvRT7OfT_yoJ9X) | Animate values and UI elements from code. |
| **UI (start here)** | [Canvas](https://youtu.be/1OwQflHq5kg) <br> [Anchors](https://youtu.be/Lf8gbfEHgcI) <br> [Placing UI in the world](https://youtu.be/Fw3uQmx-46M) <br> [Layout](https://youtu.be/HTQV4mukZ2M) <br> [Buttons](https://youtu.be/tFIFHSgYRxM) | The core of Unity UI: canvases, anchoring, world-space UI, layout groups, and buttons. |
| **UI (reference)** | [Full UI tutorial playlist](https://www.youtube.com/playlist?list=PLg0yr4zozmZVdk8ydXr1hMIqCGWklwRYw) | Covers most of the UI you will need. The five videos above come from this playlist. |

The UI videos do not use DOTween. Apply it yourself whenever you animate UI through code.

**Task:** Build some advanced UI using what you learned, and use DOTween to animate it.

## Week 7: Design patterns and architecture

| Topic | Resources | Learning Objectives |
|:--|:--|:--|
| **Organization** | [Best organization for indie games](https://youtu.be/8WqYQ1OwxJ4) <br> [Composition vs inheritance](https://youtu.be/mAfpfUYhpAs) | How to structure a project, and when to compose objects instead of inheriting. |
| **Patterns** | [Intro to some main design patterns](https://www.youtube.com/playlist?list=PLX2vGYjWbI0TmDVbWNA56NbKKUgyUAQ9i) <br> *Reference:* [All the design patterns you could need](https://www.youtube.com/playlist?list=PLnJJ5frTPwRMCCDVE_wFIt3WIj163Q81V) | The main design patterns and where they fit in game code. |
| **State machines** | [State machine basics](https://youtu.be/Vt8aZDPzRjI) <br> [Hierarchical state machine](https://youtu.be/c-XoTg6Fba4) | Build state machines for characters and game flow, then extend them into hierarchies. |

**Task:** Apply design patterns to a project.

## Week 8: Game feel and juice

| Resources | Learning Objectives |
|:--|:--|
| [Game feel and juice](https://youtu.be/216_5nu4aVQ) <br> [10 ways to improve game feel](https://youtu.be/qCj9CZoAvFY) <br> [How designers make satisfying games](https://youtu.be/TXm_7ifGZwM) <br> [Juice It or Lose It](https://www.youtube.com/watch?v=Fy0aCDmgnxg) <br> [The Art of Screenshake](https://www.youtube.com/watch?v=AJdEqssNZ-U) <br> [Juicing your cameras with math](https://www.youtube.com/watch?v=tu-Qe66AvtY) | What makes a game satisfying to play: feedback, screenshake, camera effects, and the small details that add polish. |

**Task:** Polish an old game or a new one.

## Week 9: NavMesh

| Topic | Resources | Learning Objectives |
|:--|:--|:--|
| **NavMesh** | [NavMesh basics](https://www.youtube.com/watch?v=SMWxCpLvrcc) <br> [Links and obstacles](https://www.youtube.com/watch?v=vU6fCMC_IXA) <br> [Runtime NavMesh surfaces](https://www.youtube.com/watch?v=UGh4VSeKPNA) <br> [Advanced usage](https://www.youtube.com/watch?v=JrnTHOZCzWQ) | Bake a NavMesh and move agents across it, use links and obstacles, and build NavMesh surfaces at runtime. |
| **AI (reference)** | [Full, comprehensive AI guide](https://www.youtube.com/playlist?list=PLllNmP7eq6TSkwDN8OO0E8S6CWybSE_xC) | Many hours long. Use it as a reference, not something to watch in one go. |

**Task:** Add characters that move using a NavMesh. Use at least one link or obstacle.

## Week 10: Lighting and post-processing

| Resources | Learning Objectives |
|:--|:--|
| [Lighting and post-processing guide](https://youtu.be/xhOkkGbL3mY) <br> [Changing post-processing through code](https://youtu.be/51iJqn5Px1k) <br> *Advanced:* [Advanced lighting playlist](https://www.youtube.com/playlist?list=PLSziOj2vNR-3SHp1MTsrvGAVOf2N4pvij) | Light a scene, add post-processing effects, and change them from code. |

**Task:** Light a scene of your own, add post-processing, and change at least one post-processing setting through code.

## Week 11: Shaders

| Topic | Resources | Learning Objectives |
|:--|:--|:--|
| **Start here** | [How video game graphics work](https://www.youtube.com/watch?v=C8YtdC8mxTU) <br> [What are shaders](https://youtu.be/pYgBvz9Yxuo) | How rendering works and what shaders do. |
| **Shader Graph** | [Shader Graph basics playlist](https://www.youtube.com/playlist?list=PLsaDw3p1XpJiGHPnA8gZH6gO2gQYz3JH1) | Build shaders visually. |
| **HLSL** | [HLSL shader basics playlist](https://www.youtube.com/playlist?list=PLsaDw3p1XpJivdTbFKP7cBV-WhhJ6qZ20) | Write shaders in code. |
| **Reference** | [Large shader library](https://www.youtube.com/playlist?list=PLpPd_BKEUoYjcFaqriaMchx5gOqBs2tDh) <br> [Catlike Coding](https://catlikecoding.com/) <br> [The Unity Shaders Bible (book)](https://github.com/costudiolabor/Shaders/blob/main/The%20Unity%20Shaders%20Bible%20(Jettelly).pdf) | Examples and in-depth material to look things up in. |

**Task:** Make at least one shader of your own, in Shader Graph or HLSL, and use it in a project.

## Week 12: Profiling and optimization

| Resources | Learning Objectives |
|:--|:--|
| [Profiling intro](https://youtu.be/xjsqv8nj0cw) <br> [Optimization tricks](https://youtu.be/kJ5I9md9NG4) <br> [More optimization tricks](https://www.youtube.com/watch?v=bl9pc7xaH9Q) <br> [Optimization talk](https://www.youtube.com/watch?v=S4xF-eE1pBg) | Use the Profiler to find what is slowing a game down, and fix it. |

**Task:** Profile one of your projects, find a bottleneck, and fix it. Write down the numbers before and after.

------------------------------------------------------------------------

## Level 2 Checkpoint

- Organize a project with clear structure, design patterns and ScriptableObjects.
- Build the systems a full game needs: saving, input, animation, cameras, UI and AI movement.
- Make a game look and feel good with lighting, post-processing, shaders and juice.
- Measure and improve a game's performance.
- **Checkpoint project:** one polished game on your itch.io page that uses several of these topics, with a short description of what you built and which techniques you used.

[Back to overview](../README.md) · Previous: [Beginner](../01-beginner/README.md)
