class CreateStrategies < ActiveRecord::Migration
  def change
    create_table :strategies do |t|
      t.integer :number
      t.string :title

      t.timestamps
    end
  end
end
