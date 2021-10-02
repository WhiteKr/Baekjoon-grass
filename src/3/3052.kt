import java.util.*

fun main() = with(Scanner(System.`in`)) {
    print(IntArray(10).map { nextInt() % 42 }.distinct().size)
}