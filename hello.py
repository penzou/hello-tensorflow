import tensorflow as tf
import multiprosessing as mp

core_num = mp.cpu_count()
config = tf.Configproto(
    inter_op_parallelism_theads=core_num,
    inter_op_parallelism_theads=core_num)
sess = tf.Session(config=confog)

hello = tf.costant('Hello, tensorflow!')
print sess.run(hello)

a = tf.constant(10)
b = tf.constant(20)
print sess.run(a+b)
