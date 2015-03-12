#!usr/bin/ruby

require 'minitest/autorun'
require './fizzbuzz'

class TestFizzbuzz < Minitest::Test
  def test_true_false
    assert_equal(true,true)
  end
  def test_1_donne_un
    assert_equal("1",fizzbuzz(1))
  end
  def test_2_donne_deux
    assert_equal("2",fizzbuzz(2))
  end
end
