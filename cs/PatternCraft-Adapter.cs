using System;

public class MarioAdapter : IUnit
{
    private Mario _mario;

    public MarioAdapter(Mario mario)
    {
        _mario = mario;
    }

    public void Attack(Target target)
    {
        int damage = _mario.jumpAttack();
        target.Health -= damage;
    }
}