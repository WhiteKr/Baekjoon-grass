import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val (A: Int, B: Int, V: Int) = arrayOf(nextInt(), nextInt(), nextInt())
    var pos = 0
    var count = 0
    while (pos < V) {
        pos += A
        if (pos < V) pos -= B
        ++count
    }
    print(count)
}
