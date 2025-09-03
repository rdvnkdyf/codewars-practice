public class GooseToIDuckAdapter : IDuck
{
    private Goose _goose;

    public GooseToIDuckAdapter(Goose goose)
    {
        _goose = goose;
    }

    public string Quack()
    {
        return _goose.Honk();
    }

    public void Fly()
    {
        _goose.Fly();
    }
}