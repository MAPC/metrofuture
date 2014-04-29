class CreateCounties < ActiveRecord::Migration
  def change
    create_table :counties do |t|
      t.string :name
      t.string :fips

      t.timestamps
    end

    add_column :municipalities, :county_id, :integer

  end
end