# weather_HTTP
Парсер погоды вида:

Лондон

       .-.      Light drizzle and rain
      (   ).    +2(-2) °C      
     (___(__)   ← 1 м/c        
      ‘ ‘ ‘ ‘   5 км           
     ‘ ‘ ‘ ‘    0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 18 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │      .-.      Умеренный дожд…│
│      .--.     +2(-2) °C      │     (   ).    +8(5) °C       │
│   .-(    ).   ↖ 4-7 м/c      │    (___(__)   ↑ 6-10 м/c     │
│  (___.__)__)  10 км          │   ‚‘‚‘‚‘‚‘    7 км           │
│               0.0 мм | 0%    │   ‚’‚’‚’‚’    2.8 мм | 93%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 19 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │               Пасмурно       │
│      .--.     +12(9) °C      │      .--.     +13(10) °C     │
│   .-(    ).   ↑ 8-11 м/c     │   .-(    ).   ↑ 8-12 м/c     │
│  (___.__)__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 20 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │    \  /       Переменная обл…│
│      .-.      +11(10) °C     │  _ /"".-.     +8(7) °C       │
│   ― (   ) ―   ↑ 3 м/c        │    \_(   ).   ↑ 1-2 м/c      │
│      `-’      10 км          │    /(___(__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Шереметьево

                Пасмурно
       .--.     -3(-9) °C      
    .-(    ).   → 5 м/c        
   (___.__)__)  10 км          
                0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 18 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Небольшой снег │               Пасмурно       │
│   ,\_(   ).   -2(-8) °C      │      .--.     -4(-11) °C     │
│    /(___(__)  → 5-7 м/c      │   .-(    ).   ↘ 6-8 м/c      │
│      *  *  *  10 км          │  (___.__)__)  10 км          │
│     *  *  *   0.1 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 19 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│               Облачно        │
│  _ /"".-.     -6(-12) °C     │      .--.     -5(-12) °C     │
│    \_(   ).   → 5-7 м/c      │   .-(    ).   → 6-8 м/c      │
│    /(___(__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 20 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │               Пасмурно       │
│      .-.      -5(-11) °C     │      .--.     -2(-9) °C      │
│   ― (   ) ―   ↗ 5-7 м/c      │   .-(    ).   ↗ 6-10 м/c     │
│      `-’      10 км          │  (___.__)__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Череповец

      \   /     Солнечно
       .-.      -12(-18) °C    
    ― (   ) ―   ↘ 3 м/c        
       `-’      10 км          
      /   \     0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 18 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│               Переохлаждённы…│
│  _ /"".-.     -11(-17) °C    │  _ - _ - _ -  -21(-25) °C    │
│    \_(   ).   ↘ 3-5 м/c      │   _ - _ - _   → 1-2 м/c      │
│    /(___(__)  10 км          │  _ - _ - _ -  0 км           │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 19 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Дымка          │               Дымка          │
│  _ - _ - _ -  -2(-6) °C      │  _ - _ - _ -  -6(-10) °C     │
│   _ - _ - _   → 3-4 м/c      │   _ - _ - _   ↗ 3-5 м/c      │
│  _ - _ - _ -  2 км           │  _ - _ - _ -  2 км           │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 20 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │               Дымка          │
│      .--.     -7(-11) °C     │  _ - _ - _ -  -11(-13) °C    │
│   .-(    ).   ↗ 1-3 м/c      │   _ - _ - _   ↑ 1-2 м/c      │
│  (___.__)__)  10 км          │  _ - _ - _ -  2 км           │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

