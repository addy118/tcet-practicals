wait(S)
{
    while (S <= 0)
        ; // busy waiting
    S--;
}

signal(S)
{
    S++;
}

// producer
do
{
    // produce an item
    wait(empty)
        wait(mutex)

        // place in buffer
        signal(mutex)
            signal(full)
} while (true)

    // consumer
    do
{
    wait(full)
        wait(mutex)

        // consume item from buffer
        signal(mutex)
            signal(empty)
}
while (true)
