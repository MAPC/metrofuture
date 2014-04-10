class CreateSubStrategies < ActiveRecord::Migration
  def change
    create_table :sub_strategies do |t|
      t.string :title
      t.string :letter
      t.integer :strategy_id

      t.timestamps
    end
  end
end
